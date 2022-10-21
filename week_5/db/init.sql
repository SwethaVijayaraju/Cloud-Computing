CREATE TABLE IF NOT EXISTS Meals (
    MealId SERIAL PRIMARY KEY
    ,MealName TEXT NOT NULL
    ,MealPrice REAL NOT NULL
);

INSERT INTO Meals(MealName, MealPrice) VALUES ('Masala Dosa', 9.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Ramen', 13.50);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Pop Corn Chicken', 11.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Chilli Chicken', 12.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Biriyani', 12.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Beans Parupu Usuli', 7.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Medu Vada', 6.50);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Grilled Chicken Burger', 8.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('South Indian Filter Coffee', 5.00);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Chicken Buritto', 9.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Basil Pasta', 10.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Idly Vada Pongal Combo', 10.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Fried Rice', 9.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Apple Pie', 9.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Enchilada', 10.50);