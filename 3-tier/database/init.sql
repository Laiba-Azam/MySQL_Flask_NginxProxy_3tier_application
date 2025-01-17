USE `mysql`;
CREATE TABLE `book`(
    `id` BIGINT(20) NOT NULL,
    `name` VARCHAR(255) DEFAULT NULL
);

--
-- Dumping data for table `kubedb_table`
--

INSERT INTO `book`(`id`, `name`)
VALUES(1, 'name1'),(2, 'name2'),(3, 'name3');