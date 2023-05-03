-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 03/05/2023 às 14:28
-- Versão do servidor: 8.0.31
-- Versão do PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mineracao`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `endereco` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `data_alteracao` date DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=351 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


--
-- Acionadores `clientes`
--
DROP TRIGGER IF EXISTS `Tgr_Clientes_Insert`;
DELIMITER $$
CREATE TRIGGER `Tgr_Clientes_Insert` AFTER INSERT ON `clientes` FOR EACH ROW BEGIN
	INSERT INTO TABELA_CHAVE(ID, TABELA, CARGA) VALUES(new.ID_CLIENTE, "CLIENTES", 0);
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_Clientes_Update`;
DELIMITER $$
CREATE TRIGGER `Tgr_Clientes_Update` AFTER UPDATE ON `clientes` FOR EACH ROW BEGIN

UPDATE TABELA_CHAVE SET TABELA_CHAVE.CARGA = 0 WHERE TABELA_CHAVE.TABELA = 'CLIENTES' AND TABELA_CHAVE.ID = OLD.ID_CLIENTE;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `dw_d_clientes`
--

DROP TABLE IF EXISTS `dw_d_clientes`;
CREATE TABLE IF NOT EXISTS `dw_d_clientes` (
  `ID_CLIENTE` bigint DEFAULT NULL,
  `NOME` text,
  `ENDERECO` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Acionadores `dw_d_clientes`
--
DROP TRIGGER IF EXISTS `Tgr_unflag_clients`;
DELIMITER $$
CREATE TRIGGER `Tgr_unflag_clients` AFTER INSERT ON `dw_d_clientes` FOR EACH ROW BEGIN
    UPDATE tabela_chave SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_CLIENTE;
END
$$
DELIMITER ;

-- --------------------------------------------------------


--
-- Acionadores `dw_d_livros`
--
DROP TRIGGER IF EXISTS `Tgr_unflag_livros`;
DELIMITER $$
CREATE TRIGGER `Tgr_unflag_livros` AFTER INSERT ON `dw_d_livros` FOR EACH ROW BEGIN
    UPDATE tabela_chave SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_LIVRO AND tabela_chave.tabela = 'LIVROS';
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `dw_d_lojas`
--

DROP TABLE IF EXISTS `dw_d_lojas`;
CREATE TABLE IF NOT EXISTS `dw_d_lojas` (
  `ID_LOJA` bigint DEFAULT NULL,
  `ENDERECO` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Acionadores `dw_d_lojas`
--
DROP TRIGGER IF EXISTS `Tgr_unflag_stores`;
DELIMITER $$
CREATE TRIGGER `Tgr_unflag_stores` AFTER INSERT ON `dw_d_lojas` FOR EACH ROW BEGIN
    UPDATE tabela_chave SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_LOJA AND tabela_chave.tabela = 'LOJAS';
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `extract_books`
-- (Veja abaixo para a visão atual)
--
DROP VIEW IF EXISTS `extract_books`;
CREATE TABLE IF NOT EXISTS `extract_books` (
`ID_LIVRO` int
,`TITULO` varchar(120)
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `extract_clients`
-- (Veja abaixo para a visão atual)
--
DROP VIEW IF EXISTS `extract_clients`;
CREATE TABLE IF NOT EXISTS `extract_clients` (
`ID_CLIENTE` int
,`ENDERECO` varchar(100)
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `extract_stores`
-- (Veja abaixo para a visão atual)
--
DROP VIEW IF EXISTS `extract_stores`;
CREATE TABLE IF NOT EXISTS `extract_stores` (
`ID_LOJA` int
,`ENDERECO` varchar(100)
);

-- --------------------------------------------------------

--
-- Estrutura para tabela `itens_vendas`
--

DROP TABLE IF EXISTS `itens_vendas`;
CREATE TABLE IF NOT EXISTS `itens_vendas` (
  `id_venda` int NOT NULL,
  `id_livro` int NOT NULL,
  KEY `id_venda` (`id_venda`),
  KEY `id_livro` (`id_livro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Estrutura para tabela `livros`
--

DROP TABLE IF EXISTS `livros`;
CREATE TABLE IF NOT EXISTS `livros` (
  `id_livro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(120) COLLATE utf8mb4_general_ci NOT NULL,
  `valor_compra` float NOT NULL,
  `valor_venda` float NOT NULL,
  `data_alteracao` date DEFAULT NULL,
  PRIMARY KEY (`id_livro`)
) ENGINE=InnoDB AUTO_INCREMENT=3401 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Acionadores `livros`
--
DROP TRIGGER IF EXISTS `Tgr_Livros_Insert`;
DELIMITER $$
CREATE TRIGGER `Tgr_Livros_Insert` AFTER INSERT ON `livros` FOR EACH ROW BEGIN
	INSERT INTO TABELA_CHAVE(ID, TABELA, CARGA) VALUES(new.ID_LIVRO, "LIVROS", 0);
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_Livros_Update`;
DELIMITER $$
CREATE TRIGGER `Tgr_Livros_Update` AFTER UPDATE ON `livros` FOR EACH ROW BEGIN

UPDATE TABELA_CHAVE SET TABELA_CHAVE.CARGA = 0 WHERE TABELA_CHAVE.TABELA = 'LIVROS' AND TABELA_CHAVE.ID = OLD.ID_LIVRO;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `lojas`
--

DROP TABLE IF EXISTS `lojas`;
CREATE TABLE IF NOT EXISTS `lojas` (
  `id_loja` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `faturamento_mensal` float DEFAULT NULL,
  `crescimento_mensal` float DEFAULT NULL,
  `crescimento_anual` float DEFAULT NULL,
  `endereco` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `data_alteracao` datetime DEFAULT NULL,
  PRIMARY KEY (`id_loja`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Acionadores `lojas`
--
DROP TRIGGER IF EXISTS `Tgr_Lojas_Insert`;
DELIMITER $$
CREATE TRIGGER `Tgr_Lojas_Insert` AFTER INSERT ON `lojas` FOR EACH ROW BEGIN
	INSERT INTO TABELA_CHAVE(ID, TABELA, CARGA) VALUES(new.ID_LOJA, "LOJAS", 0);
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_Lojas_Update`;
DELIMITER $$
CREATE TRIGGER `Tgr_Lojas_Update` AFTER UPDATE ON `lojas` FOR EACH ROW BEGIN

UPDATE TABELA_CHAVE SET TABELA_CHAVE.CARGA = 0 WHERE TABELA_CHAVE.TABELA = 'LOJAS' AND TABELA_CHAVE.ID = OLD.ID_LOJA;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tabela_chave`
--

DROP TABLE IF EXISTS `tabela_chave`;
CREATE TABLE IF NOT EXISTS `tabela_chave` (
  `id` int NOT NULL,
  `tabela` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `carga` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


--
-- Estrutura para tabela `vendas`
--

DROP TABLE IF EXISTS `vendas`;
CREATE TABLE IF NOT EXISTS `vendas` (
  `id_venda` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_loja` int NOT NULL,
  `valor` float NOT NULL,
  `data_venda` datetime NOT NULL,
  `data_corte` datetime NOT NULL,
  PRIMARY KEY (`id_venda`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


--
-- Estrutura para view `extract_books`
--
DROP TABLE IF EXISTS `extract_books`;

DROP VIEW IF EXISTS `extract_books`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `extract_books`  AS SELECT `a`.`id_livro` AS `ID_LIVRO`, `a`.`titulo` AS `TITULO` FROM (`livros` `a` join `tabela_chave` `b`) WHERE ((`a`.`id_livro` = `b`.`id`) AND (`b`.`tabela` = 'LIVROS') AND (`b`.`carga` = 0))  ;

-- --------------------------------------------------------

--
-- Estrutura para view `extract_clients`
--
DROP TABLE IF EXISTS `extract_clients`;

DROP VIEW IF EXISTS `extract_clients`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `extract_clients`  AS SELECT `a`.`id_cliente` AS `ID_CLIENTE`, `a`.`endereco` AS `ENDERECO` FROM (`clientes` `a` join `tabela_chave` `b`) WHERE ((`a`.`id_cliente` = `b`.`id`) AND (`b`.`tabela` = 'CLIENTES') AND (`b`.`carga` = 0))  ;

-- --------------------------------------------------------

--
-- Estrutura para view `extract_stores`
--
DROP TABLE IF EXISTS `extract_stores`;

DROP VIEW IF EXISTS `extract_stores`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `extract_stores`  AS SELECT `a`.`id_loja` AS `ID_LOJA`, `a`.`endereco` AS `ENDERECO` FROM (`lojas` `a` join `tabela_chave` `b`) WHERE ((`a`.`id_loja` = `b`.`id`) AND (`b`.`tabela` = 'LOJAS') AND (`b`.`carga` = 0))  ;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `itens_vendas`
--
ALTER TABLE `itens_vendas`
  ADD CONSTRAINT `itens_vendas_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `vendas` (`id_venda`),
  ADD CONSTRAINT `itens_vendas_ibfk_2` FOREIGN KEY (`id_livro`) REFERENCES `livros` (`id_livro`),
COMMIT;


--
-- Estrutura para tabela `dw_d_clientes`
--
DROP TABLE IF EXISTS `dw_d_clientes`;
CREATE TABLE IF NOT EXISTS `dw_d_clientes` (
  `ID_CLIENTE` INT,
  `ENDERECO` VARCHAR(150),
  `GASTOS` float(20),
  `QUANTIDADE` INT
);

CREATE TRIGGER `Tgr_unflag_clients`
AFTER INSERT ON `dw_d_clientes`
FOR EACH ROW
UPDATE `tabela_chave` SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_CLIENTE AND tabela_chave.tabela = 'CLIENTES';

--
-- Estrutura para tabela `dw_d_lojas`
--

DROP TABLE IF EXISTS `dw_d_lojas`;
CREATE TABLE IF NOT EXISTS `dw_d_lojas` (
  `ID_LOJA` INT,
  `ENDERECO` VARCHAR(150),
  `FATURAMENTO_BRUTO` FLOAT,
  `FATURAMENTO_LIQUIDO` FLOAT
);


CREATE TRIGGER Tgr_unflag_lojas
AFTER INSERT ON dw_d_lojas
FOR EACH ROW
UPDATE tabela_chave SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_LOJA AND tabela_chave.tabela = 'LOJAS';


--
-- Estrutura para tabela `dw_d_livros`
--
DROP TABLE IF EXISTS `dw_d_livros`;
CREATE TABLE IF NOT EXISTS `dw_d_livros` (
  `ID_LIVRO` INT,
  `VALOR_COMPRA` FLOAT,
  `VALOR_VENDA` FLOAT,
  `MARGEM` FLOAT
);

CREATE TRIGGER `Tgr_unflag_livros`
AFTER INSERT ON dw_d_livros
FOR EACH ROW
UPDATE tabela_chave SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_LIVRO AND tabela_chave.tabela = 'LIVROS';



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;



