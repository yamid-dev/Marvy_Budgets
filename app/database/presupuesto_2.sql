SELECT * FROM egreso;
SELECT * FROM ingreso;
SELECT * FROM compra;
SELECT * FROM usuario;
DELETE FROM egreso WHERE egreso_Id>0;
DELETE FROM usuario WHERE user_Id="YamidTarot";
DROP TABLE egreso;
DROP TABLE compra;
DROP TABLE ingreso;
DROP TABLE usuario;

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema presupuesto_2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema presupuesto_2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `presupuesto_2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `presupuesto_2` ;

-- -----------------------------------------------------
-- Table `presupuesto_2`.`usuario`
-- -----------------------------------------------------
ALTER TABLE egreso ADD egreso_Detalle VARCHAR(100);
ALTER TABLE compra ADD compra_Detalle VARCHAR(100);
ALTER TABLE ingreso ADD ingreso_Detalle VARCHAR(100);

ALTER TABLE egreso MODIFY COLUMN egreso_Fecha DATE;
ALTER TABLE compra MODIFY COLUMN compra_Fecha DATE;
ALTER TABLE ingreso MODIFY COLUMN ingreso_Fecha DATE;

DROP TABLE egreso,ingreso,compra;
ALTER TABLE egreso MODIFY COLUMN egreso_Total FLOAT GENERATED ALWAYS AS(egreso_Precio*egreso_Cantidad);
CREATE TABLE IF NOT EXISTS `presupuesto_2`.`usuario` (
  `user_Id` VARCHAR(65) NOT NULL,
  `user_Password` VARCHAR(255) NULL,
  `user_Img` LONGBLOB NULL,
  PRIMARY KEY (`user_Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `presupuesto_2`.`ingreso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `presupuesto_2`.`ingreso` (
  `ingreso_Id` INT NOT NULL,
  `ingreso_Tipo` VARCHAR(65) NULL,
  `ingreso_Cantidad` INT NULL,
  `ingreso_Precio` FLOAT NULL,
  `ingreso_Fecha` DATE NULL,
  `ingreso_Total` FLOAT GENERATED ALWAYS AS(ingreso_Precio*ingreso_Cantidad),
  `usuario_user_Id` VARCHAR(65) NOT NULL,
  PRIMARY KEY (`ingreso_Id`, `usuario_user_Id`),
  INDEX `fk_ingreso_usuario_idx` (`usuario_user_Id` ASC) VISIBLE,
  CONSTRAINT `fk_ingreso_usuario`
    FOREIGN KEY (`usuario_user_Id`)
    REFERENCES `presupuesto_2`.`usuario` (`user_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE VIEW vista_total_egresos AS
SELECT SUM(egreso_Total) AS total_egresos FROM egreso;

CREATE VIEW vista_total_ingresos AS
SELECT SUM(ingreso_Total) AS total_ingresos FROM ingreso;


DROP VIEW vista_total_egresos;

-- -----------------------------------------------------
-- Table `presupuesto_2`.`egreso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `presupuesto_2`.`egreso` (
  `egreso_Id` INT NOT NULL,
  `egreso_Tipo` VARCHAR(65) NULL,
  `egreso_Cantidad` INT NULL,
  `egreso_Precio` FLOAT NULL,
  `egreso_Fecha` INT NULL,
  `egreso_Total` FLOAT GENERATED ALWAYS AS(egreso_Precio*egreso_Cantidad),
  `usuario_user_Id` VARCHAR(65) NOT NULL,
  PRIMARY KEY (`egreso_Id`, `usuario_user_Id`),
  INDEX `fk_egreso_usuario1_idx` (`usuario_user_Id` ASC) VISIBLE,
  CONSTRAINT `fk_egreso_usuario1`
    FOREIGN KEY (`usuario_user_Id`)
    REFERENCES `presupuesto_2`.`usuario` (`user_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `presupuesto_2`.`compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `presupuesto_2`.`compra` (
  `compra_Id` INT NOT NULL,
  `compra_Tipo` VARCHAR(65) NULL,
  `compra_Cantidad` INT NULL,
  `compra_Precio` FLOAT NULL,
  `compra_Fecha` INT NULL,
  `compra_Total` FLOAT GENERATED ALWAYS AS(compra_Precio*compra_Cantidad),
  `compra_Check` TINYINT(1) NULL,
  `usuario_user_Id` VARCHAR(65) NOT NULL,
  PRIMARY KEY (`compra_Id`, `usuario_user_Id`),
  INDEX `fk_compra_usuario1_idx` (`usuario_user_Id` ASC) VISIBLE,
  CONSTRAINT `fk_compra_usuario1`
    FOREIGN KEY (`usuario_user_Id`)
    REFERENCES `presupuesto_2`.`usuario` (`user_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
