-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26-Abr-2023 às 01:31
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.1.12

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

CREATE TABLE `clientes` (
  `id` int(100) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `endereco` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Acionadores `clientes`
--
DELIMITER $$
CREATE TRIGGER `Tgr_Clientes_Insert` AFTER INSERT ON `clientes` FOR EACH ROW BEGIN
	INSERT INTO TABELA_CHAVE(ID, TABELA, CARGA) VALUES(new.ID, "CLIENTES", 0);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Tgr_Clientes_Update` AFTER UPDATE ON `clientes` FOR EACH ROW BEGIN

UPDATE TABELA_CHAVE SET TABELA_CHAVE.CARGA = 0 WHERE TABELA_CHAVE.TABELA = 'CLIENTES' AND TABELA_CHAVE.ID = OLD.ID;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `livros`
--

CREATE TABLE `livros` (
  `id` int(11) NOT NULL,
  `titulo` varchar(120) NOT NULL,
  `valor_compra` float NOT NULL,
  `valor_venda` float NOT NULL,
  `data_alteracao` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Acionadores `livros`
--
DELIMITER $$
CREATE TRIGGER `Tgr_Livros_Insert` AFTER INSERT ON `livros` FOR EACH ROW BEGIN
	INSERT INTO TABELA_CHAVE(ID, TABELA, CARGA) VALUES(new.ID, "LIVROS", 0);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Tgr_Livros_Update` AFTER UPDATE ON `livros` FOR EACH ROW BEGIN

UPDATE TABELA_CHAVE SET TABELA_CHAVE.CARGA = 0 WHERE TABELA_CHAVE.TABELA = 'LIVROS' AND TABELA_CHAVE.ID = OLD.ID;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lojas`
--

CREATE TABLE `lojas` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `faturamento_mensal` float DEFAULT NULL,
  `crescimento_mensal` float DEFAULT NULL,
  `crescimento_anual` float DEFAULT NULL,
  `endereco` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `lojas`
--


--
-- Acionadores `lojas`
--
DELIMITER $$
CREATE TRIGGER `Tgr_Lojas_Insert` AFTER INSERT ON `lojas` FOR EACH ROW BEGIN
	INSERT INTO TABELA_CHAVE(ID, TABELA, CARGA) VALUES(new.ID, "LOJAS", 0);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Tgr_Lojas_Update` AFTER UPDATE ON `lojas` FOR EACH ROW BEGIN

UPDATE TABELA_CHAVE SET TABELA_CHAVE.CARGA = 0 WHERE TABELA_CHAVE.TABELA = 'LOJAS' AND TABELA_CHAVE.ID = OLD.ID;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tabela_chave`
--

CREATE TABLE `tabela_chave` (
  `id` int(11) NOT NULL,
  `tabela` varchar(50) NOT NULL,
  `carga` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `livros`
--
ALTER TABLE `livros`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `lojas`
--
ALTER TABLE `lojas`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `tabela_chave`
--
ALTER TABLE `tabela_chave`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;

--
-- AUTO_INCREMENT de tabela `lojas`
--
ALTER TABLE `lojas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
