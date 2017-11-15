load data local infile 'RXNATOMARCHIVE.RRF' into table RXNATOMARCHIVE fields terminated by '|' 
ESCAPED BY 'ä'
lines terminated by '\n'
(@rxaui,@aui,@str,@archive_timestamp,@created_timestamp,@updated_timestamp,@code,@is_brand,@lat,@last_released,@saui,@vsab,@rxcui,@sab,@tty,@merged_to_rxcui)
SET rxaui =@rxaui,
    aui =@aui,
    str =@str,
    archive_timestamp =@archive_timestamp,
    created_timestamp =@created_timestamp,
    updated_timestamp =@updated_timestamp,
    code =@code,
    is_brand =@is_brand,
    lat =@lat,
    last_released =@last_released,
    saui =@saui,
    vsab =@vsab,
    rxcui =@rxcui,
    sab =@sab,
    tty =@tty,
    merged_to_rxcui =@merged_to_rxcui;


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
    
    
    
load data local infile 'RXNSAB.RRF' into table RXNSAB fields terminated by '|' 
 ESCAPED BY 'ä' 
 lines terminated by '\n'
(@vcui,@rcui,@vsab,@rsab,@son,@sf,@sver,@vstart,@vend,@imeta,@rmeta,@slc,@scc,@srl,@tfr,@cfr,@cxty,@ttyl,@atnl,@lat,@cenc,@curver,@sabin,@ssn,@scit)
SET vcui =@vcui,
    rcui =@rcui,
    vsab =@vsab,
    rsab=@rsab,
    son=@son,
    sf=@sf,
    sver=@sver,
    vstart=@vstart,
    vend=@vend,
    imeta=@imeta,
    rmeta=@rmeta,
    slc=@slc,
    scc=@scc,
    srl=nullif(@srl,''),
    tfr=nullif(@tfr,''),
    cfr=nullif(@cfr,''),
    cxty=@cxty,
    ttyl=@ttyl,
    atnl=@atnl,
    lat=@lat,
    cenc=@cenc,
    curver=@curver,
    sabin=@sabin,
    ssn=@ssn,
    scit=@scit;
    

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



load data local infile 'RXNSTY.RRF' into table RXNSTY fields terminated by '|' 
ESCAPED BY 'ä'
lines terminated by '\n'
(@rxcui,@tui,@stn,@sty,@atui,@cvf)
SET rxcui=@rxcui,
    tui =@tui,
    stn =@stn,
    sty =@sty,
    atui=@atui,
    cvf =@cvf;



load data local infile 'RXNDOC.RRF' into table RXNDOC fields terminated by '|' 
ESCAPED BY 'ä'
lines terminated by '\n'
(@dockey,@value,@type,@expl)
SET dockey=@dockey,
    value =@value,
    type =@type,
    expl =@expl;
    
    
load data local infile 'RXNCUICHANGES.RRF' into table RXNCUICHANGES fields terminated by '|' 
ESCAPED BY 'ä'
lines terminated by '\n'
(@rxaui,@code,@sab,@tty,@str,@old_rxcui,@new_rxcui)
SET rxaui=@rxaui,
    code =@code,
    sab =@sab,
    tty =@tty,
    str =@str,
    old_rxcui =@old_rxcui,
    new_rxcui =@new_rxcui;

load data local infile 'RXNCUI.RRF' into table RXNCUI fields terminated by '|'
ESCAPED BY 'ä'
lines terminated by '\n'
(@cui1,@ver_start,@ver_end,@cardinality,@cui2)
SET cui1=@cui1,
    ver_start =@ver_start,
    ver_end =@ver_end,
    cardinality =@cardinality,
    cui2 =@cui2;
