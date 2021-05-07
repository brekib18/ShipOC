insert into category(name) values ('Morgunkorn');
insert into category(name) values ('Bækur');
insert into category(name) values ('Föt');
insert into category(name) values ('Fylgihlutir');


insert into cereal_cerealcategory(name) values ('Vegan');
insert into cereal_cerealcategory(name) values ('Sætt');
insert into cereal_cerealcategory(name) values ('Sykurlítið');

insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Cocoa Puffs','Hver elskar ekki Cocoa Puffs? Hrikalega bragðgott.','650',1,2);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Cheerios','Eitt allra vinsælasta morgunkorn allra tíma!','420',1,3);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Weetabix','Hollt, gott og vegan!','400',1,1);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Corn Flakes','Morgunkornið sem allir elska.','580',1,1);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Barbara’s Shredded Wheat Cereal','100% sykulaust','500',1,3);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Corn Pops','600','Ómótstæðilegar morgunkúlur.',1,2);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Kashi','430','Fyrir þá sem vilja engan sykur.',1,3);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Frosted Flakes','600','Sykurhúðað Corn Flakes.',1,2);
insert into cereal_cereal(name, description, price, category_id, cereal_category_id) values ('Crispy Wheat & Raisins','440','Fullkomin máltið í skál.',1,3);

insert into cereal_cerealimage(image, cereal_id) values ('https://png2.cleanpng.com/sh/45f62e997d18b00cce9e407a492558cd/L0KzQYm3VsE6N6Ztj5H0aYP2gLBuTfJzbZJwftN8dD3mdcPsgfwuepZqi9c2cz3zhbftk71zbZZ4fZ98LYDocbB8lL1jfaV5RadrMkm3drXtUsJiOZQ9RqsAOEG4SYO4UcUzQWU4TKICOUG3QYq1kP5o/kisspng-breakfast-cereal-reese-s-puffs-reese-s-peanut-butt-5b294fdf22a1c8.9581592115294340791419.png',1);
insert into cereal_cerealimage(image, cereal_id) values ('https://www.pngitem.com/pimgs/m/546-5465420_transparent-cereal-cheerios-cheerios-cereal-hd-png-download.png',2);
insert into cereal_cerealimage(image, cereal_id) values ('https://img.favpng.com/2/6/21/breakfast-cereal-weet-bix-weetabix-whole-grain-png-favpng-37tZqytAqtrP1vCWjudM6nHb3.jpg',3);
insert into cereal_cerealimage(image, cereal_id) values ('http://images.kglobalservices.com/www.kelloggs.com.au/en_au/product/product_449/prod_img-198128_kelloggs-corn-flakes.png',4);
insert into cereal_cerealimage(image, cereal_id) values ('https://www.barbaras.com/wp-content/uploads/2019/11/Barbaras-Shredded-Wheat-Cereal-Box.png',5);
insert into cereal_cerealimage(image, cereal_id) values ('https://icon2.cleanpng.com/20180420/lre/kisspng-breakfast-cereal-kellogg-s-corn-pops-cereal-milk-a-corn-pops-5ad9d434358905.5683214115242250762193.jpg',6);
insert into cereal_cerealimage(image, cereal_id) values ('http://images.kglobalservices.com/www.kashi.com/en_us/product/product_4508544/prod_img-1107114_ks_rtec_h2h_png.png',7);
insert into cereal_cerealimage(image, cereal_id) values ('https://img.favpng.com/16/25/25/frosted-flakes-breakfast-cereal-corn-flakes-frosting-icing-png-favpng-kBRcA6Bu6esnYrqseVKjNrMZ5.jpg',8);
insert into cereal_cerealimage(image, cereal_id) values ('http://images.kglobalservices.com/www.kelloggs.ie/en_ie/product/product_253594/prod_img-253850_05053827165808_a1l1_25_uk.png',9);