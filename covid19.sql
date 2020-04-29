drop table covid19;

CREATE TABLE covid19(
	index integer,
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
	country_bef_Mexico_n integer,
	citizenship_n integer
);

select * from covid19;