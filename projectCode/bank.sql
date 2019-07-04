-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 02, 2019 at 05:27 PM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
CREATE TABLE IF NOT EXISTS `account` (
  `accno` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `deposit` int(11) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`accno`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`accno`, `name`, `type`, `deposit`, `password`) VALUES
(2, 'Aditya Deep', 'C', 3000, 'aditya'),
(3, 'chait', 's', 2990, 'chait'),
(12345, 'aditya deep', 'current', 688, '123456'),
(123456, 'adityadeep', 'c', 3000, '12345'),
(23232323, 'adi', 'c', 100, '12345'),
(855564, 'faegeAF', 'c', 2, '3343'),
(855334, 'adityaa', 'c', 6000, '777');

-- --------------------------------------------------------

--
-- Table structure for table `man`
--

DROP TABLE IF EXISTS `man`;
CREATE TABLE IF NOT EXISTS `man` (
  `manid` varchar(20) NOT NULL,
  `manpin` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `man`
--

INSERT INTO `man` (`manid`, `manpin`) VALUES
('aditya', 7777),
('muskan', 6666),
('abhinetra', 1111),
('chaitanya', 2222);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
