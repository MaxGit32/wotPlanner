
CREATE TABLE marks (
    mark_id SERIAL PRIMARY KEY,
    color TEXT,
    image TEXT NOT NULL,
    map TEXT NOT NULL,
    positionx NUMERIC NOT NULL DEFAULT 0,
    positionx2 NUMERIC NOT NULL DEFAULT 0,
    positiony NUMERIC NOT NULL DEFAULT 0,
    positiony2 NUMERIC NOT NULL DEFAULT 0,
    size NUMERIC NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE maps (
    mapName TEXT PRIMARY KEY NOT NULL,
    url TEXT NOT NULL
);

INSERT INTO maps VALUES 
    ('abbeystandard', './maps/abbeystandard.jpg'),
    ('airfieldstandard', './maps/airfieldstandard.jpg'),
    ('cliffencounter', './maps/cliffencounter.jpg'),
    ('cliffstandard', './maps/cliffstandard.jpg'),
    ('elhalufencounter', './maps/elhalufencounter.jpg'),
    ('elhalufstandard', './maps/elhalufstandard.jpg'),
    ('empiresborderstandard', './maps/empiresborderstandard.jpg'),
    ('enskencounter', './maps/enskencounter.jpg'),
    ('enskstandard', './maps/enskstandard.jpg'),
    ('erlenbergassault', './maps/erlenbergassault.jpg'),
    ('erlenbergstandard', './maps/erlenbergstandard.jpg'),
    ('fishermansbaystandard', './maps/fishermansbaystandard.jpg'),
    ('fjordsstandard', './maps/fjordsstandard.jpg'),
    ('ghosttownassault', './maps/ghosttownassault.jpg'),
    ('ghosttownencounter', './maps/ghosttownencounter.jpg'),
    ('ghosttownstandard', './maps/ghosttownstandard.jpg'),
    ('glacierstandard', './maps/glacierstandard.jpg'),
    ('highwaystandard', './maps/highwaystandard.jpg'),
    ('himmelsdorfencounter', './maps/himmelsdorfencounter.jpg'),
    ('himmelsdorfstandard', './maps/himmelsdorfstandard.jpg'),
    ('hinterlandstandard', './maps/hinterlandstandard.jpg'),
    ('kareliaassault', './maps/kareliaassault.jpg'),
    ('kareliastandard', './maps/kareliastandard.jpg'),
    ('klondikestandard', './maps/klondikestandard.jpg'),
    ('kraftwerkstandard', './maps/kraftwerkstandard.jpg'),
    ('lakevilleencounter', './maps/lakevilleencounter.jpg'),
    ('liveoaksstandard', './maps/liveoaksstandard.jpg'),
    ('malinovkastandard', './maps/malinovkastandard.jpg'),
    ('mannerheimlinestandard', './maps/mannerheimlinestandard.jpg'),
    ('minesencounter', './maps/minesencounter.jpg'),
    ('minesstandard', './maps/minesstandard.jpg'),
    ('mountainpassstandard', './maps/mountainpassstandard.jpg'),
    ('murovankaencounter', './maps/murovankaencounter.jpg'),
    ('murovankastandard', './maps/murovankastandard.jpg'),
    ('nebelburgstandard', './maps/nebelburgstandard.jpg'),
    ('normandiestandard', './maps/normandiestandard.jpg'),
    ('overlordstandard', './maps/overlordstandard.jpg'),
    ('parisstandard', './maps/parisstandard.jpg'),
    ('pilsenencounter', './maps/pilsenencounter.jpg'),
    ('pilsenstandard', './maps/pilsenstandard.jpg'),
    ('prohorovkaencounter', './maps/prohorovkaencounter.jpg'),
    ('prohorovkastandard', './maps/prohorovkastandard.jpg'),
    ('provincestandard', './maps/provincestandard.jpg'),
    ('redshireassault', './maps/redshireassault.jpg'),
    ('redshireencounter', './maps/redshireencounter.jpg'),
    ('redshirestandard', './maps/redshirestandard.jpg'),
    ('ruinbergencounter', './maps/ruinbergencounter.jpg'),
    ('ruinbergstandard', './maps/ruinbergstandard.jpg'),
    ('sandriverencounter', './maps/sandriverencounter.jpg'),
    ('sandriverstandard', './maps/sandriverstandard.jpg'),
    ('serenecoaststandard', './maps/serenecoaststandard.jpg'),
    ('siegfriedlineassault', './maps/siegfriedlineassault.jpg'),
    ('siegfriedlineencounter', './maps/siegfriedlineencounter.jpg'),
    ('siegfriedlinestandard', './maps/siegfriedlinestandard.jpg'),
    ('steppesassault', './maps/steppesassault.jpg'),
    ('steppesencounter', './maps/steppesencounter.jpg'),
    ('steppesstandard', './maps/steppesstandard.jpg'),
    ('studziankiassault', './maps/studziankiassault.jpg'),
    ('studziankistandard', './maps/studziankistandard.jpg'),
    ('tundrastandard', './maps/tundrastandard.jpg'),
    ('westfieldencounter', './maps/westfieldencounter.jpg'),
    ('westfieldstandard', './maps/westfieldstandard.jpg'),
    ('wideparkstandard', './maps/wideparkstandard.jpg');

-------------Functions-------------
CREATE OR REPLACE FUNCTION public.deleteoldmarks(_map TEXT)
RETURNS JSONB AS $$
DECLARE
    result JSONB;
BEGIN
    --Delete old rows before new inserts trought store-function
    DELETE FROM marks
    WHERE marks.map = _map;

    result := '{}';
    RETURN result;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION public.store(_color TEXT, _image TEXT, _map TEXT, _positionx NUMERIC, _positionx2 NUMERIC, _positiony NUMERIC, _positiony2 NUMERIC, _size NUMERIC, _type TEXT)
RETURNS JSONB AS $$
DECLARE 
    result JSONB;
BEGIN
    --Insert new rows
    INSERT INTO marks (color, image, map, positionx, positionx2, positiony, positiony2, size, type)
    VALUES (_color, _image, _map, _positionx, _positionx2, _positiony, _positiony2, _size, _type);

    result := '{}';
    RETURN result;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION fetchmarks(_map TEXT)
RETURNS TABLE (
    color TEXT,
    image TEXT,
    map TEXT,
    positionx NUMERIC,
    positionx2 NUMERIC,
    positiony NUMERIC,
    positiony2 NUMERIC,
    size NUMERIC,
    type TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        m.color,
        m.image,
        m.map,
        m.positionx,
        m.positionx2,
        m.positiony,
        m.positiony2,
        m.size,
        m.type
    FROM
        marks AS m
    WHERE m.map = _map;
END;
$$ LANGUAGE plpgsql;

