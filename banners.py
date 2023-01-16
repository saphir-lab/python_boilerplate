BANNER_DISPLAY = True
BANNER_SELECTION = "random"  # Possible values : 'random' or number representing index of the BANNERS array for a single selection

# To generate Banner, visit https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
BANNERS = [
r"""
  ____                              
 |  _ \                             
 | |_) | __ _ _ __  _ __   ___ _ __ 
 |  _ < / _` | '_ \| '_ \ / _ \ '__|
 | |_) | (_| | | | | | | |  __/ |   
 |____/ \__,_|_| |_|_| |_|\___|_|   
""",
r"""
   ___                        
  / _ )___ ____  ___  ___ ____
 / _  / _ `/ _ \/ _ \/ -_) __/
/____/\_,_/_//_/_//_/\__/_/   
""",
r"""
   (                                  
 ( )\     )                  (   (    
 )((_) ( /(   (      (      ))\  )(   
((_)_  )(_))  )\ )   )\ )  /((_)(()\  
 | _ )((_)_  _(_/(  _(_/( (_))   ((_) 
 | _ \/ _` || ' \))| ' \))/ -_) | '_| 
 |___/\__,_||_||_| |_||_| \___| |_|                                       
""",
r"""
▄▄▄▄·  ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄  
▐█ ▀█▪▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·▀▄ █·
▐█▀▀█▄▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄ 
██▄▪▐█▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌
·▀▀▀▀  ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀                                       
"""
]

if __name__ == "__main__":  
    if BANNER_DISPLAY:
        print("-"*20)
        print(f"Banner is enabled with {len(BANNERS)} banners defined")
        print("-"*20)
        for i, banner in enumerate(BANNERS):
          print(i, banner)
    else:
        print("Banner is disabled")
