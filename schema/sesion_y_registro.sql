-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sesion_y_registro
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sesion_y_registro` ;

-- -----------------------------------------------------
-- Schema sesion_y_registro
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sesion_y_registro` DEFAULT CHARACTER SET utf8 ;
USE `sesion_y_registro` ;

-- -----------------------------------------------------
-- Table `sesion_y_registro`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sesion_y_registro`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(72) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

USE `sesion_y_registro` ;

-- -----------------------------------------------------
-- Placeholder table for view `sesion_y_registro`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sesion_y_registro`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `sesion_y_registro`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sesion_y_registro`.`view1`;
USE `sesion_y_registro`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
