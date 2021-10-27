-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 
-- 伺服器版本： 10.4.6-MariaDB
-- PHP 版本： 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `recommandation`
--

-- --------------------------------------------------------

--
-- 資料表結構 `favor`
--

CREATE TABLE `favor` (
  `feature` varchar(50) NOT NULL,
  `uid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `favor`
--

INSERT INTO `favor` (`feature`, `uid`) VALUES
('bbb`', 1),
('aaa', 2),
('ccc', 3),
('aaa', 4),
('ccc', 5),
('red', 1),
('white', 2),
('red', 3),
('blue', 4),
('black', 5),
('bag', 1),
('bag', 2),
('wallet', 3),
('bag', 4),
('wallet', 5);

-- --------------------------------------------------------

--
-- 資料表結構 `favorite`
--

CREATE TABLE `favorite` (
  `uid` int(100) NOT NULL,
  `pid` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `favorite`
--

INSERT INTO `favorite` (`uid`, `pid`) VALUES
(1, 8),
(1, 14),
(1, 7),
(2, 9),
(2, 20),
(2, 17),
(3, 16),
(3, 2),
(3, 3),
(4, 6),
(4, 9),
(4, 8),
(5, 1),
(5, 17),
(5, 4);

-- --------------------------------------------------------

--
-- 資料表結構 `product`
--

CREATE TABLE `product` (
  `pid` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `cid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `tid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `product`
--

INSERT INTO `product` (`pid`, `name`, `cid`, `bid`, `tid`) VALUES
(1, 'a', 1, 3, 2),
(2, 'b', 1, 2, 1),
(3, 'c', 3, 5, 2),
(4, 'd', 3, 1, 2),
(5, 'e', 5, 3, 1),
(6, 'f', 1, 1, 1),
(7, 'g', 5, 5, 1),
(8, 'h', 3, 1, 1),
(9, 'i', 5, 5, 1),
(10, 'j', 2, 2, 2),
(11, 'k', 5, 4, 1),
(12, 'l', 1, 5, 2),
(13, 'm', 2, 3, 2),
(14, 'n', 5, 4, 1),
(15, 'o', 2, 1, 1),
(16, 'p', 5, 1, 2),
(17, 'q', 5, 1, 2),
(18, 'r', 3, 2, 1),
(19, 's', 4, 2, 2),
(20, 't', 5, 3, 1);

-- --------------------------------------------------------

--
-- 資料表結構 `p_brand`
--

CREATE TABLE `p_brand` (
  `bid` int(11) NOT NULL,
  `brand` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `p_brand`
--

INSERT INTO `p_brand` (`bid`, `brand`) VALUES
(1, 'aaa'),
(2, 'bbb'),
(3, 'ccc'),
(4, 'ddd'),
(5, 'eee');

-- --------------------------------------------------------

--
-- 資料表結構 `p_color`
--

CREATE TABLE `p_color` (
  `cid` int(100) NOT NULL,
  `color` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `p_color`
--

INSERT INTO `p_color` (`cid`, `color`) VALUES
(1, 'black'),
(2, 'white'),
(3, 'red'),
(4, 'blue'),
(5, 'yellow');

-- --------------------------------------------------------

--
-- 資料表結構 `p_type`
--

CREATE TABLE `p_type` (
  `tid` int(100) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `p_type`
--

INSERT INTO `p_type` (`tid`, `type`) VALUES
(1, 'bag'),
(2, 'wallet');

-- --------------------------------------------------------

--
-- 資料表結構 `record`
--

CREATE TABLE `record` (
  `uid` int(100) NOT NULL,
  `pid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `record`
--

INSERT INTO `record` (`uid`, `pid`) VALUES
(1, 4),
(1, 2),
(1, 6),
(1, 12),
(1, 19),
(2, 2),
(2, 4),
(2, 19),
(2, 14),
(2, 6),
(3, 20),
(3, 9),
(3, 10),
(3, 14),
(3, 16),
(4, 7),
(4, 5),
(4, 11),
(4, 10),
(4, 13),
(5, 5),
(5, 19),
(5, 16),
(5, 12),
(5, 1);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
