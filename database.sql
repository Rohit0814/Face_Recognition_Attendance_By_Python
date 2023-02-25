-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 29, 2021 at 05:58 AM
-- Server version: 5.1.53
-- PHP Version: 5.3.4

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `face`
--

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE IF NOT EXISTS `info` (
  `name` varchar(30) NOT NULL,
  `dept` varchar(15) NOT NULL,
  `email` varchar(40) NOT NULL,
  `pswd` varchar(15) NOT NULL,
  `img` varchar(100) NOT NULL,
  `att` int(10) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`name`, `dept`, `email`, `pswd`, `img`, `att`) VALUES
('Piyush', 'IX', 'pp', 'po', 'C:/Users/iamsh/Desktop/Face/user_image/pic2.jpg', 1),
('SHUBHAM', 'BCA', 'skgsmasher14243@gmail.com', 'asdf', 'C:/Users/iamsh/Desktop/Face/user_image/pic4.jpg', 2),
('alexa', 'BCA', 'asd@asd.com', 'asd', 'C:/Users/iamsh/Desktop/Face/user_image/pic3.jpg', 1),
('SHUBHAM', 'BCA', 'abc@xyz.com', 'asdf', 'C:/Users/iamsh/Desktop/Face/user_image/pic1.jpg', 21),
('Kailash', 'CSR', 'kaiashbhakat@gmail.com', '123', 'C:/Users/iamsh/Desktop/Face/user_image/pic5.jpg', 1),
('Abhishek', 'BBA', 'sahfbad@hbdfj.com', 'asd', 'C:/Users/iamsh/Desktop/Face/user_image/pic6.jpg', 1),
('Kunal', 'MCA', 'kunal.g15@gmail.com', 'aaa', 'C:/Users/iamsh/Desktop/Face/user_image/pic7.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `stu`
--

CREATE TABLE IF NOT EXISTS `stu` (
  `name` varchar(30) NOT NULL,
  `phone` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(10) NOT NULL,
  `img` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stu`
--

INSERT INTO `stu` (`name`, `phone`, `email`, `password`, `img`) VALUES
('Shubham Kumar Gupta', 2147483647, 'skgsmasher14243@gmail.com', 'aaa', 'C:/Users/iamsh/Desktop/Pro/user_image/pic1.jpg');
