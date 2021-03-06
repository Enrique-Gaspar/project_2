ALTER DEFAULT PRIVILEGES
FOR USER postgres
IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO postgres;

drop table if exists covidmexico;


CREATE TABLE covidmexico(
	id VARCHAR(20),
	gender integer,
	age	integer,
	indig_lang_speaker integer,
	mexican_y_n integer,
	birth_State integer,
	State_residence integer,
	migration_status integer,
	was_in_contact_with_other_case integer,
	type_health_institution integer,
	inpatient_outpatient integer,
	inpatient_date VARCHAR(20),
	date_symptoms_began VARCHAR(20),
	COVID_status integer,
	pregnancy_status integer,
	DM2 integer,
	COPD integer,
	ashtma integer,
	immunosuppression integer,
	HBP integer,
	cardiovascular integer,
	obesity integer,
	RCD integer,
	smoking_status integer,
	other_comorbility integer,
	pneumonia integer,
	icu integer,
	intubated integer,
	death_alive integer,
	date_death VARCHAR(20),
	citizenship integer,
	country_bef_Mexico integer
);

select * from covidmexico;


COPY covidmexico(id, gender, age, indig_lang_speaker, mexican_y_n, birth_State, State_residence, migration_status,
	 was_in_contact_with_other_case, type_health_institution, inpatient_outpatient, inpatient_date, date_symptoms_began,
	 COVID_status, pregnancy_status, DM2, COPD, ashtma, immunosuppression, HBP, cardiovascular,
	 obesity, RCD, smoking_status, other_comorbility, pneumonia, icu, intubated, death_alive,
	 date_death, citizenship, country_bef_Mexico) 
FROM 'C:\Users\Jan Hogewoning\Desktop\project 2\project_2\data_26apr_EG1.csv' DELIMITER ',' CSV HEADER;

