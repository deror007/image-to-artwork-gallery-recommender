def getArtDict():
    # A bunch of signet artworks, I picked 3 per style:
    art_dict = {
        "Abstract 1":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/London-people-80x80cm-acrilic-canvas-thick-frame-1400E-scaled-1.jpg",
        "Abstract 2":"https://signetcontemporaryart.com/wp-content/uploads/2022/10/IMG_4640-scaled.jpeg",
        "Abstract 3":"https://signetcontemporaryart.com/wp-content/uploads/2022/10/0f697948-5499-454f-a66f-c49726c99665.jpg",
        "Abstract 4":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/3ae0ba2b-5e55-4281-8a68-6108055b5dae-2.jpg",
        "Abstract 5":"https://signetcontemporaryart.com/wp-content/uploads/2023/08/IMG-6785-scaled.jpg",
        "Abstract 6":"https://signetcontemporaryart.com/wp-content/uploads/2023/02/Anis-434x58cm-acrylic-on-paper-220E-scaled.jpg",
        "Abstract 7":"https://signetcontemporaryart.com/wp-content/uploads/2023/10/larger-3-1.jpg",
        "Abstract 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/Autumnal-Heartbeat-2.jpg",

        "Floral 1":"https://signetcontemporaryart.com/wp-content/uploads/2023/12/Eden-80x120cm-2048x1299-1.jpg",
        "Floral 2":"https://signetcontemporaryart.com/wp-content/uploads/2023/09/I-Give-You-All-The-Love-In-My-Heart-70x70-1.jpg",
        "Floral 3":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/Wild-Flower-Meadow-scaled-1.jpg",
        "Floral 4":"https://signetcontemporaryart.com/wp-content/uploads/2023/12/IMG_7185-scaled.jpg",
        "Floral 5":"https://signetcontemporaryart.com/wp-content/uploads/2023/01/IMG_5583-4-scaled.jpg",
        "Floral 6":"https://signetcontemporaryart.com/wp-content/uploads/2022/10/image_64873272-scaled.jpg",
        "Floral 7":"https://signetcontemporaryart.com/wp-content/uploads/2023/02/dancingpoppies102x1023100.jpg",
        "Floral 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/May-Garden-oil-on-canvas-45-cm-x-73-cm-4250-1.jpg",
        

        "Pop 1":"https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1116.jpeg",
        "Pop 2":"https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1145.jpeg",
        "Pop 3":"https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1127.jpeg",
        "Pop 4":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG-3497.jpg",
        "Pop 5":"https://signetcontemporaryart.com/wp-content/uploads/2023/09/1901-scaled.jpg",
        "Pop 6":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/James-Bond-Sean-Connery-Art-by-Peter-Engels-00-scaled-1.jpg",
        "Pop 7":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/Winston-Churchill-Art-by-Peter-Engels-00-scaled-1.jpg",
        "Pop 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/Queen-Elisabeth-II-portrait-painting-Art-by-Peter-Engels-01-scaled-1.jpg",


        "Wildlife 1":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/2202NAN_102x021_6.jpeg",
        "Wildlife 2":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/2202NAN_102x021_5.jpeg",
        "Wildlife 3":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/Clash1.jpg",
        "Wildlife 4":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/2110NAN_100x100_14.jpeg",
        "Wildlife 5":"https://signetcontemporaryart.com/wp-content/uploads/2023/07/African-Elephant-scaled.jpg",
        "Wildlife 6":"https://signetcontemporaryart.com/wp-content/uploads/2023/07/Catherine-4-scaled.jpg",
        "Wildlife 7":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/LR_03_29_2022_RPP_InglebyFineArt_HotPink_100x100cm.jpeg",
        "Wildlife 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/Fox-sketch.jpeg",

        "Seascape 1":"https://signetcontemporaryart.com/wp-content/uploads/2023/12/Changing-Chapters-scaled.jpg",
        "Seascape 2":"https://signetcontemporaryart.com/wp-content/uploads/2023/12/eugihub-instagram-.jpg",
        "Seascape 3":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/DarkBlueWaves50cmx50cmLennyCornforthOiloncanvas.jpg",
        "Seascape 4":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/DSC018261.jpeg",
        "Seascape 5":"https://signetcontemporaryart.com/wp-content/uploads/2023/12/Exhale-scaled.jpg",
        "Seascape 6":"https://signetcontemporaryart.com/wp-content/uploads/2023/10/siren-90x61cm.jpeg",
        "Seascape 7":"https://signetcontemporaryart.com/wp-content/uploads/2023/08/Turquoise-Tranquility-Coral-Beach-Isle-of-Skye-1000x80cm-2900-scaled.jpg",
        "Seascape 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/12/Golden-Deck-scaled.jpg",
        
        
        "Cityscape 1":"https://signetcontemporaryart.com/wp-content/uploads/2022/10/103-Afternoon-Shower-Fleet-Street-oil-60-x-60-cm.jpg",
        "Cityscape 2":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/96-Evening-Stroll-Albert-Bridge-30-x-30-cm-oil_edited-1.jpg",
        "Cityscape 3":"https://signetcontemporaryart.com/wp-content/uploads/2023/12/Misty-Backlight-scaled.jpg",
        "Cityscape 4":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/FullSizeRender2.jpg",
        "Cityscape 5":"https://signetcontemporaryart.com/wp-content/uploads/2022/10/4-AHK-London-XV-116x89x4-scaled.jpg",
        "Cityscape 6":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/The-Mousetrap-scaled-1.jpg",
        "Cityscape 7":"https://signetcontemporaryart.com/wp-content/uploads/2022/10/102-October-Sunshine-Southbank-oil-60-x-60-cm.jpg",
        "Cityscape 8":"https://signetcontemporaryart.com/wp-content/uploads/2023/05/Walking-On-By_20-x-20-inches_acrylic-on-board_2023-scaled.jpg",

        "Mongolian 1":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/4-1.jpg",
        "Mongolian 2":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/2-1.jpg",
        "Mongolian 3":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/211.jpg",
        "Mongolian 4":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/5-1.jpg",
        "Mongolian 5":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/71-1.jpg",
        "Mongolian 6":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/9-1.jpg",
        "Mongolian 7":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/12-1.jpg",
        "Mongolian 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/81.jpg",

        "Landscape 1":"https://signetcontemporaryart.com/wp-content/uploads/2023/11/Let-us-walk-in-the-light.-Autumn.-91-x-91cm-2.jpg",
        "Landscape 2":"https://signetcontemporaryart.com/wp-content/uploads/2023/11/Memories.-91-x-91cm.jpg",
        "Landscape 3":"https://signetcontemporaryart.com/wp-content/uploads/2023/04/IMG_20230327_175743-scaled.jpg",
        "Landscape 4":"https://signetcontemporaryart.com/wp-content/uploads/2023/12/Sonco-Carrasco_Tea-time-scaled.jpeg",
        "Landscape 5":"https://signetcontemporaryart.com/wp-content/uploads/2023/04/Treeline-Sunset-OC-30x30-2022-4500-lores-scaled.jpg",
        "Landscape 6":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/blossom-in-the-river-1-scaled-1.jpg",
        "Landscape 7":"https://signetcontemporaryart.com/wp-content/uploads/2022/11/IMG_6537.jpeg",
        "Landscape 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG_3186.jpg",

        "Sculpture 1":"https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1501-2-scaled.jpg",
        "Sculpture 2":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/fullsizeoutput_14e0.jpeg",
        "Sculpture 3":"https://signetcontemporaryart.com/wp-content/uploads/2022/10/h800-735756luIRrlHr.jpg",
        "Sculpture 4":"https://signetcontemporaryart.com/wp-content/uploads/2023/02/G01-1V8-2-scaled.jpg",
        "Sculpture 5":"https://signetcontemporaryart.com/wp-content/uploads/2023/07/Screenshot_20220114-222744_Collect.jpg",
        "Sculpture 6":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/FB05-1V6-1.jpg",
        "Sculpture 7":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG_8731-scaled-3.jpg",
        "Sculpture 8":"https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG_8883-scaled-3.jpg",

    }

    return art_dict

def getArtPageDict():
    shop_dict= {
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/London-people-80x80cm-acrilic-canvas-thick-frame-1400E-scaled-1.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/london-people-cubism-painting/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/10/IMG_4640-scaled.jpeg":"https://signetcontemporaryart.com/shop/still-life-paintings/london-beer-still-life/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/10/0f697948-5499-454f-a66f-c49726c99665.jpg":"https://signetcontemporaryart.com/shop/still-life-paintings/the-green-table/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/3ae0ba2b-5e55-4281-8a68-6108055b5dae-2.jpg":"https://signetcontemporaryart.com/shop/abstract-paintings/dama-desnuda/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/08/IMG-6785-scaled.jpg":"https://signetcontemporaryart.com/shop/abstract-paintings/flower-intrigue/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/02/Anis-434x58cm-acrylic-on-paper-220E-scaled.jpg":"https://signetcontemporaryart.com/shop/still-life-paintings/anis/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/10/larger-3-1.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/cafe-society/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/Autumnal-Heartbeat-2.jpg":"https://signetcontemporaryart.com/shop/landscape-paintings/autumnal-heartbeat-2/",

        "https://signetcontemporaryart.com/wp-content/uploads/2023/12/Eden-80x120cm-2048x1299-1.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/eden/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/09/I-Give-You-All-The-Love-In-My-Heart-70x70-1.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/i-give-you-all-the-love-in-my-heart/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/Wild-Flower-Meadow-scaled-1.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/wild-flower-meadow/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/12/IMG_7185-scaled.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/autumn-forest/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/01/IMG_5583-4-scaled.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/bluebell-forest-3/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/10/image_64873272-scaled.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/fall-arrangment/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/02/dancingpoppies102x1023100.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/luscious-cream-roses-copy/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/May-Garden-oil-on-canvas-45-cm-x-73-cm-4250-1.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/may-garden/",
        

        "https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1116.jpeg":"https://signetcontemporaryart.com/shop/figurative-paintings/nme-bowie/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1145.jpeg":"https://signetcontemporaryart.com/shop/figurative-paintings/rolling-stone-jimi/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1127.jpeg":"https://signetcontemporaryart.com/shop/figurative-paintings/vanity-fair-marilyn/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG-3497.jpg":"https://signetcontemporaryart.com/shop/figurative-paintings/bridget-bardot-biting-her-lip/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/09/1901-scaled.jpg":"https://signetcontemporaryart.com/shop/figurative-paintings/audrey-hepburn-vogue-red/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/James-Bond-Sean-Connery-Art-by-Peter-Engels-00-scaled-1.jpg":"https://signetcontemporaryart.com/shop/figurative-paintings/james-bond-sean-connery-shaken-not-stirred/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/Winston-Churchill-Art-by-Peter-Engels-00-scaled-1.jpg":"https://signetcontemporaryart.com/shop/figurative-paintings/winston-churchill-original-painting/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/Queen-Elisabeth-II-portrait-painting-Art-by-Peter-Engels-01-scaled-1.jpg":"https://signetcontemporaryart.com/shop/figurative-paintings/queen-elisabeth-ii/",


        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/2202NAN_102x021_6.jpeg":"https://signetcontemporaryart.com/shop/wildlife-paintings/live-it-up/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/2202NAN_102x021_5.jpeg":"https://signetcontemporaryart.com/shop/wildlife-paintings/powerful-protection/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/Clash1.jpg":"https://signetcontemporaryart.com/shop/wildlife-paintings/clash/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/2110NAN_100x100_14.jpeg":"https://signetcontemporaryart.com/shop/wildlife-paintings/arctic-shaftesbury/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/07/African-Elephant-scaled.jpg":"https://signetcontemporaryart.com/shop/wildlife-paintings/african-elephant/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/07/Catherine-4-scaled.jpg":"https://signetcontemporaryart.com/shop/wildlife-paintings/coloured-stripes/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/LR_03_29_2022_RPP_InglebyFineArt_HotPink_100x100cm.jpeg":"https://signetcontemporaryart.com/shop/wildlife-paintings/flamingo/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/Fox-sketch.jpeg":"https://signetcontemporaryart.com/shop/wildlife-paintings/fox-2/",

        "https://signetcontemporaryart.com/wp-content/uploads/2023/12/Changing-Chapters-scaled.jpg":"https://signetcontemporaryart.com/shop/seascape-paintings/changing-chapters/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/12/eugihub-instagram-.jpg":"https://signetcontemporaryart.com/shop/seascape-paintings/amazing/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/DarkBlueWaves50cmx50cmLennyCornforthOiloncanvas.jpg":"https://signetcontemporaryart.com/shop/landscape-paintings/dark-blue-waves/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/DSC018261.jpeg":"https://signetcontemporaryart.com/shop/figurative-paintings/breaking-surf/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/12/Exhale-scaled.jpg":"https://signetcontemporaryart.com/shop/seascape-paintings/exhale/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/10/siren-90x61cm.jpeg":"https://signetcontemporaryart.com/shop/figurative-paintings/siren/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/08/Turquoise-Tranquility-Coral-Beach-Isle-of-Skye-1000x80cm-2900-scaled.jpg":"https://signetcontemporaryart.com/shop/seascape-paintings/turquoise-tranquility-coral-beach-isle-of-skye/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/12/Golden-Deck-scaled.jpg":"https://signetcontemporaryart.com/shop/still-life-paintings/golden-deck/",
        
        
        "https://signetcontemporaryart.com/wp-content/uploads/2022/10/103-Afternoon-Shower-Fleet-Street-oil-60-x-60-cm.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/afternoon-shower-fleet-street-london-painting/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/96-Evening-Stroll-Albert-Bridge-30-x-30-cm-oil_edited-1.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/evening-stroll/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/12/Misty-Backlight-scaled.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/misty-backlight/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/FullSizeRender2.jpg":"https://signetcontemporaryart.com/shop/landscape-paintings/menton/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/10/4-AHK-London-XV-116x89x4-scaled.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/london-xv/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/The-Mousetrap-scaled-1.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/mousetrap/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/10/102-October-Sunshine-Southbank-oil-60-x-60-cm.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/october-sunshine-southbank-cityscape-painting/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/05/Walking-On-By_20-x-20-inches_acrylic-on-board_2023-scaled.jpg":"https://signetcontemporaryart.com/shop/cityscape-paintings/walking-on-by/",

        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/4-1.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/ballerina/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/2-1.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/behind-the-stage/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/211.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/ballerina-2/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/5-1.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/violinist/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/71-1.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/portrait-woman/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/9-1.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/queen/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/12-1.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/sunny-day/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/81.jpg":"https://signetcontemporaryart.com/shop/mongolian-art/melody/",

        "https://signetcontemporaryart.com/wp-content/uploads/2023/11/Let-us-walk-in-the-light.-Autumn.-91-x-91cm-2.jpg":"https://signetcontemporaryart.com/shop/landscape-paintings/let-us-walk-in-the-light/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/11/Memories.-91-x-91cm.jpg":"https://signetcontemporaryart.com/shop/landscape-paintings/light-and-shadows/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/04/IMG_20230327_175743-scaled.jpg":"https://signetcontemporaryart.com/shop/landscape-paintings/spring-forest-i/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/12/Sonco-Carrasco_Tea-time-scaled.jpeg":"https://signetcontemporaryart.com/shop/floral-paintings/tea-time/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/04/Treeline-Sunset-OC-30x30-2022-4500-lores-scaled.jpg":"https://signetcontemporaryart.com/shop/landscape-paintings/treeline-sunset-landscape-painting/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/blossom-in-the-river-1-scaled-1.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/blossom-on-the-river/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/11/IMG_6537.jpeg":"https://signetcontemporaryart.com/shop/landscape-paintings/always-in-my-dream/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG_3186.jpg":"https://signetcontemporaryart.com/shop/floral-paintings/forest-morning/",

        "https://signetcontemporaryart.com/wp-content/uploads/2023/07/IMG_1501-2-scaled.jpg":"https://signetcontemporaryart.com/shop/sculptures/disc-receiving-the-sun-bronze-sculpture/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/fullsizeoutput_14e0.jpeg":"https://signetcontemporaryart.com/shop/sculptures/angel-fish-3/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/10/h800-735756luIRrlHr.jpg":"https://signetcontemporaryart.com/shop/sculptures/debora-lima-pink-hue/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/02/G01-1V8-2-scaled.jpg":"https://signetcontemporaryart.com/shop/sculptures/life-is-short-relax/",
        "https://signetcontemporaryart.com/wp-content/uploads/2023/07/Screenshot_20220114-222744_Collect.jpg":"https://signetcontemporaryart.com/shop/sculptures/million-dollar-mickey/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/FB05-1V6-1.jpg":"https://signetcontemporaryart.com/shop/wildlife-paintings/puffin-whats-down/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG_8731-scaled-3.jpg":"https://signetcontemporaryart.com/shop/figurative-paintings/appearance-x/",
        "https://signetcontemporaryart.com/wp-content/uploads/2022/09/IMG_8883-scaled-3.jpg":"https://signetcontemporaryart.com/shop/wildlife-paintings/sphynx-cat-ii/",
    }

    return shop_dict
