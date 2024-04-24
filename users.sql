-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2024 at 10:54 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `province` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `major` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `created_at`, `name`, `email`, `province`, `city`, `major`) VALUES
(1, '2024-04-21 18:09:39', 'Asghar Asghari', 'asghargamer1390@gmail.com', 'Tehran', 'Tehran', 'CS'),
(3, '2024-04-21 18:33:05', 'Mamad sedighi', 'mamad007@gmail.com', 'Tehran', 'Karaj', 'CS'),
(5, '2024-04-23 12:14:34', 'Adams Mozi', 'moozi@yahoo.com', 'Gilan', 'Rasht', 'Cooking'),
(7, '2024-04-23 19:53:46', 'Kurt Cobain', 'kurt@gmail.com', 'Gilan', 'Rasht', 'Music'),
(10, '2024-04-23 20:42:58', 'Nelson Mandela', 'mandela@hotmail.com', 'Hormozgan', 'Minab', 'Politics'),
(11, '2024-04-23 20:47:53', 'Dorbine Sony', 'doorbyn@yahoo.com', 'Khorasan Razavi', 'Mashhad', 'Photography'),
(12, '2024-04-23 20:50:11', 'Steve Jobs', 'jobs@apple.com', 'Ghazvin', 'Ghazvin', 'Tech'),
(13, '2024-04-23 20:51:36', 'Magnus Carlsen', 'magnos@gmail.com', 'Tehran', 'Tehran', 'Chess'),
(14, '2024-04-23 20:53:34', 'Peepo Happy', 'pep@twitch.com', 'Tehran', 'Damavand', 'Media');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
