dari  mengetik  import  Dict , List , Union
dari  musik  impor  db

blacklist_chatdb  =  db . daftar hitamObrolan

async  def  blacklisted_chats () ->  daftar :
    obrolan  =  blacklist_chatdb . temukan ({ "chat_id" : { "$lt" : 0 }})
    kembalikan [ chat [ "chat_id" ] untuk  chat  di  waiting  chats . to_list ( panjang = 10000000000 )]


async  def  blacklist_chat ( chat_id : int ) ->  bool :
    jika  tidak  menunggu  blacklist_chatdb . find_one ({ "chat_id" : chat_id }):
        menunggu  blacklist_chatdb . insert_one ({ "chat_id" : chat_id })
        kembali  Benar
    kembali  Salah


async  def  whitelist_chat ( chat_id : int ) ->  bool :
    jika  menunggu  blacklist_chatdb . find_one ({ "chat_id" : chat_id }):
        menunggu  blacklist_chatdb . delete_one ({ "chat_id" : chat_id })
        kembali  Benar
    kembali  Salah
