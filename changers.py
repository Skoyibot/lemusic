dari  mengetik  import  Dict , List , Union


async  def  int_to_alpha ( user_id : int ) ->  str :
    alfabet  = [ "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" ]
    teks  =  ""
    user_id  =  str ( user_id )
    untuk  saya  di  user_id :
        teks  +=  alfabet [ int ( i )]
    kembalikan  teks


async  def  alpha_to_int ( user_id_alphabet : str ) ->  int :
    alfabet  = [ "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" ]
    id_pengguna  =  ""
    untuk  saya  di  user_id_alphabet :
        indeks  =  abjad . indeks ( saya )
        user_id  +=  str ( indeks )
    user_id  =  int ( user_id )
    kembalikan  user_id


def  time_to_seconds ( waktu ):
    stringt  =  str ( waktu )
     jumlah pengembalian (
        int ( x ) *  60  **  i  untuk  i , x  dalam  enumerate ( terbalik ( stringt . split ( ":" )))
    )


def  detik_to_min ( detik ):
    jika  detik  bukan None : _  
        detik  =  int ( detik )
        d , h , m , s  = (
            detik  // ( 3600  *  24 ),
            detik  //  3600  %  24 ,
            detik  %  3600  //  60 ,
            detik  %  3600  %  60 ,
        )
        jika  d  >  0 :
            kembalikan  "{:02d}:{:02d}:{:02d}:{:02d}" . format ( d , h , m , s )
        elif  h  >  0 :
            kembalikan  "{:02d}:{:02d}:{:02d}" . format ( h , m , s )
        elif  m  >  0 :
            kembalikan  "{:02d}:{:02d}" . format ( m , s )
        elif  s  >  0 :
            kembalikan  "00:{:02d}" . format ( s )
    kembali  "-"
