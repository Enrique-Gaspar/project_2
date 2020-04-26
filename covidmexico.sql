drop table if exists covidmexico;

CREATE TABLE covidmexico(
	index integer,
	id VARCHAR(30),
	gender integer,
	age	integer,
	indig_lang_speaker integer,
	mexican_y_n integer,
	birth_State integer,
	State_residence integer PRIMARY KEY,
	migration_status integer,
	citizenship VARCHAR(30),
	country_bef_Mexico VARCHAR(30),
	was_in_contact_with_other_case integer,
	type_health_institution integer,
	inpatient_outpatient integer,
	inpatient_date date,
	date_symptoms_began date,
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
	date_death date	
);


select * from covidmexico