-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 21-Maio-2023 às 20:59
-- Versão do servidor: 8.0.31
-- versão do PHP: 8.0.26

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
-- Estrutura da tabela `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `endereco` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `data_alteracao` date DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Acionadores `clientes`
--
DROP TRIGGER IF EXISTS `Tgr_after_insert_clients`;
DELIMITER $$
CREATE TRIGGER `Tgr_after_insert_clients` AFTER INSERT ON `clientes` FOR EACH ROW INSERT INTO tabela_chave(data_op, id, id_modelo, tabela, carga) VALUES (now(), NEW.ID_CLIENTE, 4, 'CLIENTES', 0)
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_after_update_clients`;
DELIMITER $$
CREATE TRIGGER `Tgr_after_update_clients` AFTER UPDATE ON `clientes` FOR EACH ROW INSERT INTO tabela_chave(data_op, id, id_modelo, tabela, carga) VALUES (now(), NEW.ID_CLIENTE, 4, 'CLIENTES', 0)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `dw_d_clientes`
--

DROP TABLE IF EXISTS `dw_d_clientes`;
CREATE TABLE IF NOT EXISTS `dw_d_clientes` (
  `ID_CLIENTE` int DEFAULT NULL,
  `ENDERECO` varchar(150) DEFAULT NULL,
  `GASTOS` float DEFAULT NULL,
  `QUANTIDADE` int DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Acionadores `dw_d_clientes`
--
DROP TRIGGER IF EXISTS `Tgr_unflag_clients`;
DELIMITER $$
CREATE TRIGGER `Tgr_unflag_clients` AFTER INSERT ON `dw_d_clientes` FOR EACH ROW UPDATE `tabela_chave` SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_CLIENTE AND tabela_chave.tabela = 'CLIENTES'
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `dw_d_livros`
--

DROP TABLE IF EXISTS `dw_d_livros`;
CREATE TABLE IF NOT EXISTS `dw_d_livros` (
  `ID_LIVRO` int DEFAULT NULL,
  `CATEGORIA` text NOT NULL,
  `VALOR_COMPRA` float DEFAULT NULL,
  `VALOR_VENDA` float DEFAULT NULL,
  `MARGEM` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Acionadores `dw_d_livros`
--
DROP TRIGGER IF EXISTS `Tgr_unflag_livros`;
DELIMITER $$
CREATE TRIGGER `Tgr_unflag_livros` AFTER INSERT ON `dw_d_livros` FOR EACH ROW UPDATE tabela_chave SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_LIVRO AND tabela_chave.tabela = 'LIVROS'
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `dw_d_lojas`
--

DROP TABLE IF EXISTS `dw_d_lojas`;
CREATE TABLE IF NOT EXISTS `dw_d_lojas` (
  `ID_LOJA` int DEFAULT NULL,
  `ENDERECO` varchar(150) DEFAULT NULL,
  `FATURAMENTO_BRUTO` float DEFAULT NULL,
  `FATURAMENTO_LIQUIDO` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Acionadores `dw_d_lojas`
--
DROP TRIGGER IF EXISTS `Tgr_unflag_lojas`;
DELIMITER $$
CREATE TRIGGER `Tgr_unflag_lojas` AFTER INSERT ON `dw_d_lojas` FOR EACH ROW UPDATE tabela_chave SET CARGA = 1 WHERE tabela_chave.id = NEW.ID_LOJA AND tabela_chave.tabela = 'LOJAS'
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `dw_f_vendas`
--

DROP TABLE IF EXISTS `dw_f_vendas`;
CREATE TABLE IF NOT EXISTS `dw_f_vendas` (
  `SURROGATE` bigint NOT NULL,
  `ID_VENDA` bigint DEFAULT NULL,
  `ID_LOJA` bigint DEFAULT NULL,
  `VALOR` double DEFAULT NULL,
  `DATA_VENDA` datetime DEFAULT NULL,
  `DATA_CORTE` datetime DEFAULT NULL,
  `ID_LIVRO` bigint DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `etl_controle`
--

DROP TABLE IF EXISTS `etl_controle`;
CREATE TABLE IF NOT EXISTS `etl_controle` (
  `id_etl` bigint NOT NULL AUTO_INCREMENT,
  `tabela` varchar(100) NOT NULL,
  `id_modelo` int NOT NULL,
  `data_ultimo_corte` datetime DEFAULT NULL,
  PRIMARY KEY (`id_etl`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura stand-in para vista `extract_books`
-- (Veja abaixo para a view atual)
--
DROP VIEW IF EXISTS `extract_books`;
CREATE TABLE IF NOT EXISTS `extract_books` (
`ID_LIVRO` int
,`CATEGORIA` text
,`VALOR_COMPRA` float
,`VALOR_VENDA` float
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para vista `extract_clients`
-- (Veja abaixo para a view atual)
--
DROP VIEW IF EXISTS `extract_clients`;
CREATE TABLE IF NOT EXISTS `extract_clients` (
`ID_CLIENTE` int
,`ENDERECO` varchar(100)
,`GASTOS` double
,`QUANTIDADE` bigint
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para vista `extract_stores`
-- (Veja abaixo para a view atual)
--
DROP VIEW IF EXISTS `extract_stores`;
CREATE TABLE IF NOT EXISTS `extract_stores` (
`ID_LOJA` int
,`ENDERECO` varchar(100)
,`FATURAMENTO_BRUTO` double
,`FATURAMENTO_LIQUIDO` double
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `itens_vendas`
--

DROP TABLE IF EXISTS `itens_vendas`;
CREATE TABLE IF NOT EXISTS `itens_vendas` (
  `id_venda` int NOT NULL,
  `id_livro` int NOT NULL,
  KEY `id_venda` (`id_venda`),
  KEY `id_livro` (`id_livro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `livros`
--

DROP TABLE IF EXISTS `livros`;
CREATE TABLE IF NOT EXISTS `livros` (
  `id_livro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `categoria` text COLLATE utf8mb4_general_ci NOT NULL,
  `valor_compra` float NOT NULL,
  `valor_venda` float NOT NULL,
  `data_alteracao` date DEFAULT NULL,
  PRIMARY KEY (`id_livro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Acionadores `livros`
--
DROP TRIGGER IF EXISTS `Tgr_after_insert_books`;
DELIMITER $$
CREATE TRIGGER `Tgr_after_insert_books` AFTER INSERT ON `livros` FOR EACH ROW INSERT INTO tabela_chave(data_op, id, id_modelo, tabela, carga) VALUES (now(), NEW.ID_LIVRO, 3, 'LIVROS', 0)
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_after_update_books`;
DELIMITER $$
CREATE TRIGGER `Tgr_after_update_books` AFTER UPDATE ON `livros` FOR EACH ROW INSERT INTO tabela_chave(data_op, id, id_modelo, tabela, carga) VALUES (now(), NEW.ID_LIVRO, 3, 'LIVROS', 0)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lojas`
--

DROP TABLE IF EXISTS `lojas`;
CREATE TABLE IF NOT EXISTS `lojas` (
  `id_loja` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `endereco` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `data_alteracao` datetime DEFAULT NULL,
  PRIMARY KEY (`id_loja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Acionadores `lojas`
--
DROP TRIGGER IF EXISTS `Tgr_after_insert_stores`;
DELIMITER $$
CREATE TRIGGER `Tgr_after_insert_stores` AFTER INSERT ON `lojas` FOR EACH ROW INSERT INTO tabela_chave(data_op, id, id_modelo, tabela, carga) VALUES (now(), NEW.ID_LOJA, 2, 'LOJAS', 0)
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Tgr_after_update_stores`;
DELIMITER $$
CREATE TRIGGER `Tgr_after_update_stores` AFTER UPDATE ON `lojas` FOR EACH ROW INSERT INTO tabela_chave(data_op, id, id_modelo, tabela, carga) VALUES (now(), NEW.ID_LOJA, 2, 'LOJAS', 0)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `modelos`
--

DROP TABLE IF EXISTS `modelos`;
CREATE TABLE IF NOT EXISTS `modelos` (
  `id_modelo` int NOT NULL AUTO_INCREMENT,
  `assunto` varchar(100) NOT NULL,
  `servidor_origem` varchar(100) NOT NULL,
  `servidor_destino` varchar(100) NOT NULL,
  PRIMARY KEY (`id_modelo`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tabela_chave`
--

DROP TABLE IF EXISTS `tabela_chave`;
CREATE TABLE IF NOT EXISTS `tabela_chave` (
  `delta_id` int NOT NULL AUTO_INCREMENT,
  `data_op` datetime NOT NULL,
  `id` int NOT NULL,
  `id_modelo` int NOT NULL,
  `tabela` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `carga` tinyint(1) NOT NULL,
  PRIMARY KEY (`delta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendas`
--

DROP TABLE IF EXISTS `vendas`;
CREATE TABLE IF NOT EXISTS `vendas` (
  `id_venda` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_loja` int NOT NULL,
  `valor` float NOT NULL,
  `data_venda` datetime NOT NULL,
  `data_corte` datetime DEFAULT NULL,
  PRIMARY KEY (`id_venda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para vista `extract_books`
--
DROP TABLE IF EXISTS `extract_books`;

DROP VIEW IF EXISTS `extract_books`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `extract_books`  AS SELECT `a`.`id_livro` AS `ID_LIVRO`, `a`.`categoria` AS `CATEGORIA`, `a`.`valor_compra` AS `VALOR_COMPRA`, `a`.`valor_venda` AS `VALOR_VENDA` FROM (`livros` `a` join `tabela_chave` `b`) WHERE ((`a`.`id_livro` = `b`.`id`) AND (`b`.`tabela` = 'LIVROS') AND (`b`.`carga` = 0))  ;

-- --------------------------------------------------------

--
-- Estrutura para vista `extract_clients`
--
DROP TABLE IF EXISTS `extract_clients`;

DROP VIEW IF EXISTS `extract_clients`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `extract_clients`  AS SELECT `a`.`id_cliente` AS `ID_CLIENTE`, `a`.`endereco` AS `ENDERECO`, sum(`c`.`valor`) AS `GASTOS`, count(`d`.`id_venda`) AS `QUANTIDADE` FROM (((`clientes` `a` join `tabela_chave` `b`) join `vendas` `c`) join `itens_vendas` `d`) WHERE ((`a`.`id_cliente` = `b`.`id`) AND (`b`.`tabela` = 'CLIENTES') AND (`b`.`carga` = 0) AND (`c`.`id_cliente` = `a`.`id_cliente`) AND (`c`.`id_venda` = `d`.`id_venda`)) GROUP BY `a`.`id_cliente``id_cliente`  ;

-- --------------------------------------------------------

--
-- Estrutura para vista `extract_stores`
--
DROP TABLE IF EXISTS `extract_stores`;

DROP VIEW IF EXISTS `extract_stores`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `extract_stores`  AS SELECT `a`.`id_loja` AS `ID_LOJA`, `a`.`endereco` AS `ENDERECO`, sum(`c`.`valor`) AS `FATURAMENTO_BRUTO`, sum((`e`.`valor_venda` - `e`.`valor_compra`)) AS `FATURAMENTO_LIQUIDO` FROM ((((`lojas` `a` join `tabela_chave` `b`) join `vendas` `c`) join `itens_vendas` `d`) join `livros` `e`) WHERE ((`a`.`id_loja` = `b`.`id`) AND (`b`.`tabela` = 'LOJAS') AND (`b`.`carga` = 0) AND (`c`.`id_loja` = `a`.`id_loja`) AND (`c`.`id_loja` = `a`.`id_loja`) AND (`c`.`id_venda` = `d`.`id_venda`) AND (`d`.`id_livro` = `e`.`id_livro`)) GROUP BY `a`.`id_loja``id_loja`  ;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `itens_vendas`
--
ALTER TABLE `itens_vendas`
  ADD CONSTRAINT `itens_vendas_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `vendas` (`id_venda`),
  ADD CONSTRAINT `itens_vendas_ibfk_2` FOREIGN KEY (`id_livro`) REFERENCES `livros` (`id_livro`),
COMMIT;


CREATE VIEW EXTRACT_CLIENTS AS SELECT A.ID_CLIENTE, A.ENDERECO,  SUM(C.VALOR) AS 'GASTOS', COUNT(D.ID_VENDA) AS 'QUANTIDADE' FROM CLIENTES A, TABELA_CHAVE B, VENDAS C, ITENS_VENDAS D WHERE A.ID_CLIENTE = B.ID AND B.TABELA = 'CLIENTES' AND B.CARGA = 0 AND C.ID_CLIENTE = A.ID_CLIENTE AND C.ID_VENDA = D.ID_VENDA GROUP BY A.ID_CLIENTE;

CREATE VIEW EXTRACT_STORES AS SELECT A.ID_LOJA, A.ENDERECO, SUM(C.VALOR) AS 'FATURAMENTO_BRUTO', SUM(E.VALOR_VENDA-E.VALOR_COMPRA) AS 'FATURAMENTO_LIQUIDO' FROM LOJAS A, TABELA_CHAVE B, VENDAS C, ITENS_VENDAS D, LIVROS E WHERE A.ID_LOJA = B.ID AND B.TABELA = 'LOJAS' AND B.CARGA = 0 AND C.ID_LOJA = A.ID_LOJA AND C.ID_LOJA = A.ID_LOJA AND C.ID_VENDA = D.ID_VENDA AND D.ID_LIVRO = E.ID_LIVRO  GROUP by A.ID_LOJA;

CREATE VIEW EXTRACT_BOOKS AS SELECT A.ID_LIVRO, A.CATEGORIA, A.VALOR_COMPRA, A.VALOR_VENDA FROM LIVROS A, TABELA_CHAVE B WHERE A.ID_LIVRO = B.ID AND B.TABELA = 'LIVROS' AND B.CARGA = 

CREATE VIEW EXTRACT_SELLS AS SELECT A.ID_LIVRO, A.VALOR_COMPRA, A.VALOR_VENDA FROM LIVROS A, TABELA_CHAVE B WHERE A.ID_LIVRO = B.ID AND B.TABELA = 'LIVROS' AND B.CARGA = 0

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
