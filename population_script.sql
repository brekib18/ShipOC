insert into frontpage_category(name) values ('Morgunkorn');
insert into frontpage_category(name) values ('Bækur');
insert into frontpage_category(name) values ('Föt');
insert into frontpage_category(name) values ('Fylgihlutir');


insert into cereal_cerealcategory(name) values ('Vegan');
insert into cereal_cerealcategory(name) values ('Sætt');
insert into cereal_cerealcategory(name) values ('Sykurlítið');


-- CEREAL
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Cocoa Puffs','Hver elskar ekki Cocoa Puffs? Hrikalega bragðgott. Cocoa puffs inniheldur sykur, litarefni, hafra, sterkju, rotvarnarefni og egg.','650',37,29,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Cheerios','Eitt allra vinsælasta morgunkorn allra tíma! Cheerios innihledur rotvarnarefni, maíssterkju, ýruefni, salt, bindiefni, vítamín, steinefni og hafra.','420',37,30,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Weetabix','Hollt, gott og vegan!','400',37,28,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Corn Flakes','Morgunkornið sem allir elska.','580',37,28,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Barbara’s Shredded Wheat Cereal','100% sykulaust','500',37,30,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Corn Pops','Ómótstæðilegar morgunkúlur.','600',37,29,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Kashi','Fyrir þá sem vilja engan sykur.','430',37,30,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Frosted Flakes','Sykurhúðað Corn Flakes.','600',37,29,False);
insert into cereal_cereal(name, description, price, category_id_id, cereal_category_id_id,on_sale) values ('Crispy Wheat & Raisins','Fullkomin máltið í skál.','440',37,30,False);

insert into cereal_cerealimage(image1,image2, cereal_id) values ('https://cereals.generalmills.com/wp-content/uploads/2019/04/cocoa-puffs.png','https://img2.pngio.com/foodcolgate-cocoa-puffs-png-314_240.png',46);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('https://www.pngitem.com/pimgs/m/546-5465420_transparent-cereal-cheerios-cheerios-cereal-hd-png-download.png','https://pngimage.net/wp-content/uploads/2018/05/bowl-of-cheerios-png-2.png',47);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('https://img.favpng.com/2/6/21/breakfast-cereal-weet-bix-weetabix-whole-grain-png-favpng-37tZqytAqtrP1vCWjudM6nHb3.jpg','https://cdn-a.william-reed.com/var/wrbm_gb_food_pharma/storage/images/7/8/0/0/1680087-1-eng-GB/Weetabix-contract-dragged-food-recycler-into-administration_wrbm_large.png',48);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('http://images.kglobalservices.com/www.kelloggs.com.au/en_au/product/product_449/prod_img-198128_kelloggs-corn-flakes.png','https://www.pngarea.com/pngm/54/655757_corn-png-bowl-of-corn-flakes-png-download.png',49);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('https://www.barbaras.com/wp-content/uploads/2019/11/Barbaras-Shredded-Wheat-Cereal-Box.png','https://spy.com/wp-content/uploads/2021/03/Overlay-Recovered-Recovered-19.png',50);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('https://icon2.cleanpng.com/20180420/lre/kisspng-breakfast-cereal-kellogg-s-corn-pops-cereal-milk-a-corn-pops-5ad9d434358905.5683214115242250762193.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSCx_gcwpEhB-kfJ9u4vM4g-GzcUo9bCNkYQ&usqp=CAU',51);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('http://images.kglobalservices.com/www.kashi.com/en_us/product/product_4508544/prod_img-1107114_ks_rtec_h2h_png.png','https://www.kelloggs.com/content/dam/NorthAmerica/kelloggs/en_US/images/BrandDetail/Kashi/Kashi_1880x835_hero-image.jpg',52);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('https://img.favpng.com/16/25/25/frosted-flakes-breakfast-cereal-corn-flakes-frosting-icing-png-favpng-kBRcA6Bu6esnYrqseVKjNrMZ5.jpg','https://www.pngarea.com/pngm/54/655757_corn-png-bowl-of-corn-flakes-png-download.png',53);
insert into cereal_cerealimage(image1,image2, cereal_id) values ('http://images.kglobalservices.com/www.kelloggs.ie/en_ie/product/product_253594/prod_img-253850_05053827165808_a1l1_25_uk.png','https://upload.wikimedia.org/wikipedia/commons/2/2b/Frosted_Mini_Wheats.PNG',54);

-- BOOKS
insert into books_books(name, description, price, category_id_id) values ('The Cheerios Play Book','Frábær bók um Cheerios fyrir alla krakka.','350',38);
insert into books_books(name, description, price, category_id_id) values ('The Great American Cereal Book: How Breakfast Got Its Crunch','Þessi bók er skyldueign fyrir alla sem elska morgunkorn.','410',38);
insert into books_books(name, description, price, category_id_id) values ('Cold Cereal','Sprenghlægileg bók um morgunkorn og allt sem því tengist.','450',38);
insert into books_books(name, description, price, category_id_id) values ('Champions of Breakfast','Frábærar uppskrifir sem allar innihalda morgunkorn.','380',38);


insert into books_booksimage(image, cereal_id) values ('https://images-na.ssl-images-amazon.com/images/I/51yyZPvaVcL.jpg',46);
insert into books_booksimage(image, cereal_id) values ('https://images-na.ssl-images-amazon.com/images/I/51oHcj4BHUL._SX377_BO1,204,203,200_.jpg',47);
insert into books_booksimage(image, cereal_id) values ('https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1337049786l/13621768.jpg',48);
insert into books_booksimage(image, cereal_id) values ('https://images-na.ssl-images-amazon.com/images/I/51u4LbWWQdL._SX329_BO1,204,203,200_.jpg',49);

-- clothes

insert into clothes_clothes(name, description, price, category_id) values ('Cocoa Puffs','Flottur Cocoa Puffs bolur sem klæðir alla vel!','2.350',39);
insert into clothes_clothes(name, description, price, category_id) values ('Cheerios','Mjúkur og hlýr bolur með Cheerios logo-inu','2.150',39);
insert into clothes_clothes(name, description, price, category_id) values ('Apple Jacks','Nýtískuleg og flott peysa','1.999',39);


insert into clothes_clothesimage(image, clothes_id) values ('https://c0.klipartz.com/pngpicture/427/99/sticker-png-ringer-t-shirt-clothing-amazon-com-t-shirt-tshirt-brown-fashion-vintage-clothing-top.png',1);
insert into clothes_clothesimage(image, clothes_id) values ('https://img1.pnghut.com/7/12/19/8NvYLZhab5/tshirt-hood-clothing-bluza-sweater.jpg',2);
insert into clothes_clothesimage(image, clothes_id) values ('https://cdn.shopify.com/s/files/1/0670/6431/products/33840_2048x2048.png?v=1571153389',3);

-- accessories

insert into accessories_accessories(name, description, price, category_id) values ('Cheerios mjólkurkanna','Flott Cheerios mjólkurkanna sem tekur 1L.',2.650,40);
insert into accessories_accessories(name, description, price, category_id) values ('Cheerios bolli','Glæsilegur Cheerios plastbolli. Tilvalinn til að borða Cheerios úr.','2.150',39);
insert into accessories_accessories(name, description, price, category_id) values ('Frosted flakes sokkar','Frábærir og góðir sokkar','1.999',39);


insert into accessories_accessoriesimage(image, clothes_id) values ('https://i.ebayimg.com/images/g/dEMAAOSwBxBc1uX1/s-l400.jpg',1);
insert into accessories_accessoriesimage(image, clothes_id) values ('https://i.pinimg.com/originals/c1/78/d5/c178d5f54976844b156c6fc4d71d6ff9.jpg',2);
insert into accessories_accessoriesimage(image, clothes_id) values ('https://cdn.shopify.com/s/files/1/0317/1509/products/FF_BACK.jpg',3);
