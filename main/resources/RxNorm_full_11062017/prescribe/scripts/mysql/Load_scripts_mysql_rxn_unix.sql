load data local infile 'RXNCONSO.RRF' into table RXNCONSO fields terminated by '|' 
ESCAPED BY 'ä'
lines terminated by '\n'
(@rxcui,@lat,@ts,@lui,@stt,@sui,@ispref,@rxaui,@saui,@scui,@sdui,@sab,@tty,@code,@str,@srl,@suppress,@cvf)
SET rxcui =@rxcui,
    lat =@lat,
    ts =@ts,
    lui =@lui,
    stt =@stt,
    sui =@sui,
    ispref =@ispref,
    rxaui =@rxaui,
    saui =@saui,
    scui =@scui,
    sdui =@sdui,
    sab =@sab,
    tty =@tty,
    code =@code,
    str =@str,
    srl =@srl,
    suppress=@suppress,
    cvf=@cvf;


load data local infile 'RXNREL.RRF' into table RXNREL fields terminated by '|' 
ESCAPED BY 'ä'
lines terminated by '\n'
(@rxcui1,@rxaui1,@stype1,@rel,@rxcui2,@rxaui2,@stype2,@rela,@rui,@srui,@sab,@sl,@rg,@dir,@suppress,@cvf)
SET rxcui1 =@rxcui1,
    rxaui1 =@rxaui1,
    stype1 =@stype1,
    rel =@rel,
    rxcui2 =@rxcui2,
    rxaui2 =@rxaui2,
    stype2 =@stype2,
    rela =@rela,
    rui=@rui,
    srui=@srui,
    sab =@sab,
    sl =@sl,
    rg=@rg,
    dir=@dir,
    suppress=@suppress,
    cvf=@cvf;
    

load data local infile 'RXNSAT.RRF' into table RXNSAT fields terminated by '|' 
ESCAPED BY 'ä'
lines terminated by '\n'
(@rxcui,@lui,@sui,@rxaui,@stype,@code,@atui,@satui,@atn,@sab,@atv,@suppress,@cvf)
SET rxcui=@rxcui,
    lui =@lui,
    sui =@sui,
    rxaui=@rxaui,
    stype =@stype,
    code =@code,
    atui =@atui,
    satui =@satui,
    atn =@atn,
    sab=@sab,
    atv =@atv,
    suppress =@suppress,
    cvf =@cvf;



