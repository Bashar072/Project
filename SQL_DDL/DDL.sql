 User  | CREATE TABLE `User` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Email` varchar(40) NOT NULL,
  `Role` varchar(20) DEFAULT NULL,
  `Is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Id`)
)


Students | CREATE TABLE `Students` (
  `Pid` varchar(20) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `Dept_name` varchar(20) NOT NULL,
  `Course_Name` varchar(40) NOT NULL,
  `CGPA` float(4,2) DEFAULT NULL,
  `Semester` int(3) DEFAULT NULL,
  `Description` varchar(150) DEFAULT NULL,
  `Date_of_birth` date DEFAULT NULL,
  PRIMARY KEY (`Pid`)
)


Company | CREATE TABLE `Company` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Location` varchar(30) NOT NULL,
  `website` varchar(50) NOT NULL,
  `Email` varchar(40) NOT NULL,
  PRIMARY KEY (`Id`)
)



Job_Posting | CREATE TABLE `Job_Posting` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Company_id` int(11) DEFAULT NULL,
  `Eligibility` varchar(150) NOT NULL,
  `Application_Open_Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Application_Close_Date` datetime NOT NULL,
  `Location` varchar(40) NOT NULL,
  `Job_Description` varchar(250) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Company_id` (`Company_id`),
  CONSTRAINT `Job_Posting_ibfk_1` FOREIGN KEY (`Company_id`) REFERENCES `Company` (`Id`)
)



Job_Applications | CREATE TABLE `Job_Applications` (
  `Company_id` int(11) DEFAULT NULL,
  `student_id` varchar(20) DEFAULT NULL,
  `Application_Date` datetime NOT NULL,
  KEY `Company_id` (`Company_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `Job_Applications_ibfk_1` FOREIGN KEY (`Company_id`) REFERENCES `Company` (`Id`),
  CONSTRAINT `Job_Applications_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Students` (`Pid`)
)
