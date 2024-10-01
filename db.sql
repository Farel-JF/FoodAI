CREATE DATABASE FoodAI;
USE FoodAI;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE `FoodAI`.`Orders` (
  `Order_id` INT NOT NULL,
  `User_id` INT NOT NULL,
  `Status` VARCHAR(45) NULL,
  `Total_amount` DECIMAL(10, 2) NULL,  -- Specify precision and scale
  `Order_date` TIMESTAMP NULL,         -- Remove invalid precision
  `User_id_1` INT NULL,
  PRIMARY KEY (`Order_id`, `User_id`)
);
CREATE TABLE `FoodAI`.`Users` (
  `User_id` INT NOT NULL,
  `Password` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Goal` TEXT NULL,  -- TEXT type does not require a length
  `Diet_preference` INT NULL,
  `Created_at` TIMESTAMP NULL,  -- No precision
  `Name` VARCHAR(45) NULL,
  PRIMARY KEY (`User_id`)
);
