BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "clv_patient" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"code"	TEXT,
	"gender"	TEXT,
	"birthday"	TEXT,
	"phase_id"	INTEGER,
	"phase"	TEXT,
	"address_name"	TEXT,
	"street_name"	TEXT,
	"street"	TEXT,
	"street_number"	TEXT,
	"street2"	TEXT,
	"street_number2"	TEXT,
	"zip"	TEXT,
	"city_id"	INTEGER,
	"city"	TEXT,
	"state_id"	INTEGER,
	"country_state"	TEXT,
	"country_id"	INTEGER,
	"country"	TEXT,
	"mobile"	INTEGER,
	"email"	INTEGER,
	"marker_ids"	TEXT,
	"markers"	TEXT,
	"ext_id"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "clv_patient_marker" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"description"	TEXT,
	"color"	INTEGER,
	"active"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "clv_phase" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"description"	TEXT,
	"ext_id"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "host" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"server"	TEXT NOT NULL,
	"dbname"	TEXT NOT NULL,
	"user"	TEXT NOT NULL,
	"user_pw"	TEXT,
	"user_apikey"	TEXT,
	"master_pw"	INTEGER,
	"notes"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "res_company" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"ext_id"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "res_country" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"code"	TEXT,
	"ext_id"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "res_partner" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"type"	TEXT,
	"ext_id"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "res_users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"partner_id"	INTEGER,
	"company_id"	INTEGER,
	"parent_id"	INTEGER,
	"tz"	TEXT,
	"lang"	TEXT,
	"country_id"	INTEGER,
	"login"	TEXT,
	"password"	TEXT,
	"active"	INTEGER,
	"image_1920"	TEXT,
	"ext_id"	INTEGER,
	PRIMARY KEY("id")
);
CREATE UNIQUE INDEX "idx_clv_patient_code" ON "clv_patient" (
	"code"	ASC
);
CREATE INDEX "idx_clv_patient_name" ON "clv_patient" (
	"name"	ASC
);
COMMIT;
