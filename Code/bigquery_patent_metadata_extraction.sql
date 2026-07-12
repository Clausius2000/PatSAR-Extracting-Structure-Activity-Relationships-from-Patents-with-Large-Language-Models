#standardSQL



WITH input AS (

  SELECT *

  FROM UNNEST([

    /*

    Example:

    Replace the following placeholder records with your own patent identifiers.

    Use standardized publication numbers in the format used by Google Patents / BigQuery,

    such as WO-2021247748-A1, CN-113717157-B, or US-12084443-B2.

    */



    STRUCT(1 AS input_index, 'RAW_PATENT_NUMBER_1' AS raw_input, 'STANDARDIZED_PUBLICATION_NUMBER_1' AS standardized_publication_number),

    STRUCT(2 AS input_index, 'RAW_PATENT_NUMBER_2' AS raw_input, 'STANDARDIZED_PUBLICATION_NUMBER_2' AS standardized_publication_number),

    STRUCT(3 AS input_index, 'RAW_PATENT_NUMBER_3' AS raw_input, 'STANDARDIZED_PUBLICATION_NUMBER_3' AS standardized_publication_number)

  ])

)



SELECT

  i.input_index,

  i.raw_input,

  i.standardized_publication_number AS input_publication_number,



  CASE

    WHEN p.publication_number IS NULL THEN 'NOT_MATCHED'

    ELSE 'MATCHED'

  END AS match_status,



  p.publication_number,

  p.application_number,

  p.country_code AS jurisdiction,

  p.kind_code,



  CASE

    WHEN p.country_code = 'WO' AND REGEXP_CONTAINS(p.kind_code, r'^A') THEN 'PCT application publication'

    WHEN REGEXP_CONTAINS(p.kind_code, r'^A') THEN 'Patent application publication'

    WHEN REGEXP_CONTAINS(p.kind_code, r'^(B|C|T)') THEN 'Granted patent publication'

    WHEN p.grant_date IS NOT NULL AND p.grant_date != 0 THEN 'Granted patent publication'

    ELSE 'Other or unclear'

  END AS document_type_inferred,



  CASE

    WHEN p.country_code = 'WO' AND REGEXP_CONTAINS(p.kind_code, r'^A') THEN 'Application'

    WHEN REGEXP_CONTAINS(p.kind_code, r'^A') THEN 'Application'

    WHEN REGEXP_CONTAINS(p.kind_code, r'^(B|C|T)') THEN 'Granted'

    WHEN p.grant_date IS NOT NULL AND p.grant_date != 0 THEN 'Granted'

    ELSE 'Other or unclear'

  END AS patent_status_inferred,



  SAFE.PARSE_DATE('%Y%m%d', CAST(NULLIF(p.publication_date, 0) AS STRING)) AS publication_date,

  EXTRACT(YEAR FROM SAFE.PARSE_DATE('%Y%m%d', CAST(NULLIF(p.publication_date, 0) AS STRING))) AS publication_year,

  SAFE.PARSE_DATE('%Y%m%d', CAST(NULLIF(p.filing_date, 0) AS STRING)) AS filing_date,

  SAFE.PARSE_DATE('%Y%m%d', CAST(NULLIF(p.grant_date, 0) AS STRING)) AS grant_date,



  ARRAY_TO_STRING(p.assignee, '; ') AS assignees_raw,



  (

    SELECT STRING_AGG(DISTINCT a.name, '; ' ORDER BY a.name)

    FROM UNNEST(p.assignee_harmonized) AS a

    WHERE a.name IS NOT NULL

  ) AS assignees_harmonized,



  (

    SELECT STRING_AGG(DISTINCT ipc.code, '; ' ORDER BY ipc.code)

    FROM UNNEST(p.ipc) AS ipc

    WHERE ipc.code IS NOT NULL

  ) AS ipc_all,



  (

    SELECT STRING_AGG(DISTINCT SUBSTR(ipc.code, 1, 4), '; ' ORDER BY SUBSTR(ipc.code, 1, 4))

    FROM UNNEST(p.ipc) AS ipc

    WHERE ipc.code IS NOT NULL

  ) AS ipc_subclass_all,



  (

    SELECT STRING_AGG(DISTINCT cpc.code, '; ' ORDER BY cpc.code)

    FROM UNNEST(p.cpc) AS cpc

    WHERE cpc.code IS NOT NULL

  ) AS cpc_all,



  (

    SELECT STRING_AGG(DISTINCT SUBSTR(cpc.code, 1, 4), '; ' ORDER BY SUBSTR(cpc.code, 1, 4))

    FROM UNNEST(p.cpc) AS cpc

    WHERE cpc.code IS NOT NULL

  ) AS cpc_subclass_all



FROM input AS i

LEFT JOIN `patents-public-data.patents.publications` AS p

ON p.publication_number = i.standardized_publication_number



ORDER BY i.input_index;
