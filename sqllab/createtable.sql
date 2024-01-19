DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime text,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magType text,
  nst text,
  gap text,
  dmin text,
  rms text,
  net text,
  id text,
  place text,
  horizontalError text,
  depthError text, 
  magError text, 
  magNst text,
  locationSource text,
  magSource text
);