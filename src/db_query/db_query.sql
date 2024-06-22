SELECT rr.PATIENT_ID
      ,rr.ORDER_ID
      ,rr.REPORT_ID
  FROM radiology.report AS rr


  JOIN patient.demographics AS pd
  ON rr.PATIENT_ID = pd.PATIENT_ID
  JOIN radiology.order_tbl AS ro
  ON rr.order_id = ro.order_ID 

WHERE pd.dod is Null
AND pd.dob < '2006-01-01 00:00:00'
AND ro.created_date > '2024-01-01 00:00:00' 
AND ro.created_date < '2024-04-01 00:00:00' 