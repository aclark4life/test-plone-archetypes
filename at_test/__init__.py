from Products.Archetypes.atapi import listTypes as list_types
from Products.Archetypes.atapi import process_types
from Products.CMFCore import utils


PERMISSION = 'at_test: Add testtype'
PROJECTNAME = 'at_test'


def Y_U_NO_INIT(context):
    """
                         ________  ____  _____ ____     ____ __  __ _____ 
                        |__  / _ \|  _ \| ____|___ \   / ___|  \/  |  ___|
                          / / | | | |_) |  _|   __) | | |   | |\/| | |_   
                         / /| |_| |  __/| |___ / __/  | |___| |  | |  _|  
                        /____\___/|_|   |_____|_____|  \____|_|  |_|_|    
                                                                          
                            _    ____   ____ _   _ _____ _______   ______  _____ ____  
                           / \  |  _ \ / ___| | | | ____|_   _\ \ / /  _ \| ____/ ___| 
                          / _ \ | |_) | |   | |_| |  _|   | |  \ V /| |_) |  _| \___ \ 
                         / ___ \|  _ <| |___|  _  | |___  | |   | | |  __/| |___ ___) |
                        /_/   \_\_| \_\\____|_| |_|_____| |_|   |_| |_|   |_____|____/ 
                                                               

                                            `..-:///////::--.`                                      
                                    ` `-+shhddhyyoooooosyyyhddhso/.`                                
                                -+ymNddhs/.``                `.:+yddhs/.                            
                             .omdss+/.`          -.             `  `./ydds/.                        
                          `+dms:`               .o.             -s-  `+.-/yddo-`                    
                        -smy:`                   --         `    /d- .:o`  `-ohdy/`                 
                     `/hdo.                          `-.   `-.    sh`  -:`     ./ydy:`              
                    .dm+.                                   `-:.  `ho  /+//:`     .+hds-            
                   .hd-                                        ::` -y` //....::-`   `-sms.          
                  `hN-                                    .     `+. o. `  `+o-`        -hm+         
                  +N+                            `.---.` `/.     `::-/` `::`            `oms`       
                 -ms`                             ```.:++:.+y:`    `:/:-/`                -md-      
                .dd.                            `-::-::-.-+-:dms/`   .s+.       `-         -hm:     
               `hm-                            :+-.+o+.`.-.::-yNdy+``:/s:``..:+yo-`         `hm-    
               /N+                             o. +MMNh. `:`-``yo/::-``.--+dNho+//::-.`      .dd.   
              .dh`                             :. .sdh/..`:   .dmo:``.-::-:ys.-/:---:---`     -Ns`  
              oN/                              `.-.-:+---/` `/s+:/s:--..-.+y-o-::.://---`      oN/  
             `md`                             `://::::-..--/::.  `::``.:/.-o-o/``/NMNd-:`      .md` 
             +N+                              `.:-:+//:-..`` `.    `   ..`.:+//...shy+.:`       oN: 
            .dh`                             .+-.     ````-/:-``           `os-.--/---.`        -my 
            :No                              `--`  :/+yso+/-   /-.````      `s/......           `ym.
            :N+                                     `.``       -hsos+::.```  +s````..            sm.
            :N+                                                +yo/syyo+-:.``-:o-                sm.
            :N+                                               .d/-.```.os/-/:`-oh-               sm.
            :No                                               -d+:/+:-```` `:`.:::               ym.
            :Ns                                              .+-.`.-/os/`       ./              `dd`
            .dd.                       ``                    o+ ```  `/y:.`   `:+.              :Ns 
             oN:              `-.      ``                   `+/.-++/-`.+mdhyyhho`               sN- 
             -Ny               -.              .-`          .yhmNNmho:-/y/:+hhh.               `md` 
             `mm`                               `           `ydNms-.``.-://:/hy/-              :Ns  
              yN-                                           -+yo:/-:ooshdh+.`:dd+`             sN:  
              :Ns                            .`             -+.`-+ys/:::++//+`oy:             `mh`  
              `sN:                     ``                  `s++oo+-s./-//oo+/`oo              /M/   
               .dd.                    -:`                 /ssodmNdmss+y:+//-sms             .dd`   
                -dd.                                      -o/yosmhss+o+yhyh+s/+:`           `ym:    
                 .hd/`                                   `-  .-::o:///o/y/:so``..          -ym/     
                  `sdy/-`                                .  `.` `-.--.:.:. .+..          `/mh-      
                  `-yNmmd/.                        `-  `:::++/+:.`     ``  -:          `:hd/`       
                `:hds-`./ydy:.                    .o. `:-ooo///osss+/:....:os`       `+dd+.         
              ./hd+.      ./yhy+-`              .os.  /o:-       `.-:/+//:.`so`  `.:sdh/`           
            .+dh/` .:-`      ./shhs/-``     `.:so:`  `+:                    -m+/syhyo-`             
         `-sdy:`   -sdh:        `-+yhhys+:--+ys-     `. .                `./smds+:`                 
       .+hds-        .smo.           `-/oydmmdso+/::-...-.`````````.--/+shdy+-`                     
    `-odh:`            -ym+`              ``.-:/+osyyhhhhdmmdhhhhhdhhys+:.`                  ``     
  `/hdy-                 /mh:`                          -yNs-``````                   -s-   -N+     
.odh/`                    `/mh:`                      `+mhhdy-`    `  `.              -ymy+/sN/oy.  
md:                         .+dh/                    -dm/..:odd/` .do +mo `/-          .dmydNNdd/   
s.                            `ody/`                :mh:`````-+dds:dm-:Nh`:Ns       `-smy- `...`    
                                `odh/`            `+mh.``....-:ohNNNMmmMmhdd/-`  `-+hdo-            
                                  `+hd+`    `````:yNhoooosyhddhs+-.oNd+ohNdydh--oddy:`              
                                     /dm++syddddNNdsso++/:-.`       -smy::/+syhms-                  
                                      `oy+:-` `sN/                    .omddmh/-`                    
                                             `+No                       `::`                        
                                            `+mo`                                                   
                                           `oNs`                                                    
   ` ``    `  `  ` `  `  `   ` `          .sN+                                                      
`  `````````` ```  `` `` ``  ```  ```    `+d/                                                       
                           __   __  _   _   _   _  ___    ___ _   _ ___ _____ 
                           \ \ / / | | | | | \ | |/ _ \  |_ _| \ | |_ _|_   _|
                            \ V /  | | | | |  \| | | | |  | ||  \| || |  | |  
                             | |   | |_| | | |\  | |_| |  | || |\  || |  | |  
                             |_|    \___/  |_| \_|\___/  |___|_| \_|___| |_|  
                                                                              
                           __   _____  _   _ ____  ____  _____ _     _____ ___ _ 
                           \ \ / / _ \| | | |  _ \/ ___|| ____| |   |  ___|__ \ |
                            \ V / | | | | | | |_) \___ \|  _| | |   | |_    / / |
                             | || |_| | |_| |  _ < ___) | |___| |___|  _|  |_||_|
                             |_| \___/ \___/|_| \_\____/|_____|_____|_|    (_)(_)
    """
    types = list_types(PROJECTNAME)
    content_types, constructors, ftis = process_types(types, PROJECTNAME)
    all_types = zip(content_types, constructors)
    for content_type, constructor in all_types:
        kind = "%s: %s" % (PROJECTNAME, content_type.archetype_name)
        content = ContentInit(kind, content_types=(content_type,),
            permission=PERMISSION, extra_constructors=(constructor,),
        )
        content.initialize(context)
