/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `serviciosbanco` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `serviciosbanco`;

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add tb alumno', 7, 'add_tbalumno'),
	(26, 'Can change tb alumno', 7, 'change_tbalumno'),
	(27, 'Can delete tb alumno', 7, 'delete_tbalumno'),
	(28, 'Can view tb alumno', 7, 'view_tbalumno'),
	(29, 'Can add cuenta alumnos', 8, 'add_cuentaalumnos'),
	(30, 'Can change cuenta alumnos', 8, 'change_cuentaalumnos'),
	(31, 'Can delete cuenta alumnos', 8, 'delete_cuentaalumnos'),
	(32, 'Can view cuenta alumnos', 8, 'view_cuentaalumnos'),
	(33, 'Can add cuent alumnos', 8, 'add_cuentalumnos'),
	(34, 'Can change cuent alumnos', 8, 'change_cuentalumnos'),
	(35, 'Can delete cuent alumnos', 8, 'delete_cuentalumnos'),
	(36, 'Can view cuent alumnos', 8, 'view_cuentalumnos'),
	(37, 'Can add tb deudas alumno', 9, 'add_tbdeudasalumno'),
	(38, 'Can change tb deudas alumno', 9, 'change_tbdeudasalumno'),
	(39, 'Can delete tb deudas alumno', 9, 'delete_tbdeudasalumno'),
	(40, 'Can view tb deudas alumno', 9, 'view_tbdeudasalumno'),
	(41, 'Can add tb pagos alumno', 10, 'add_tbpagosalumno'),
	(42, 'Can change tb pagos alumno', 10, 'change_tbpagosalumno'),
	(43, 'Can delete tb pagos alumno', 10, 'delete_tbpagosalumno'),
	(44, 'Can view tb pagos alumno', 10, 'view_tbpagosalumno'),
	(45, 'Can add tb cuenta', 11, 'add_tbcuenta'),
	(46, 'Can change tb cuenta', 11, 'change_tbcuenta'),
	(47, 'Can delete tb cuenta', 11, 'delete_tbcuenta'),
	(48, 'Can view tb cuenta', 11, 'view_tbcuenta');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(8, 'ServicioEducacion', 'cuentalumnos'),
	(7, 'ServicioEducacion', 'tbalumno'),
	(11, 'ServicioEducacion', 'tbcuenta'),
	(9, 'ServicioEducacion', 'tbdeudasalumno'),
	(10, 'ServicioEducacion', 'tbpagosalumno'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'ServicioEducacion', '0001_initial', '2023-04-28 10:01:07.778293'),
	(2, 'contenttypes', '0001_initial', '2023-04-28 10:01:11.211062'),
	(3, 'auth', '0001_initial', '2023-04-28 10:01:31.958663'),
	(4, 'admin', '0001_initial', '2023-04-28 10:01:35.476847'),
	(5, 'admin', '0002_logentry_remove_auto_add', '2023-04-28 10:01:35.550046'),
	(6, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-28 10:01:35.635553'),
	(7, 'contenttypes', '0002_remove_content_type_name', '2023-04-28 10:01:37.441099'),
	(8, 'auth', '0002_alter_permission_name_max_length', '2023-04-28 10:01:39.127963'),
	(9, 'auth', '0003_alter_user_email_max_length', '2023-04-28 10:01:39.611629'),
	(10, 'auth', '0004_alter_user_username_opts', '2023-04-28 10:01:40.023704'),
	(11, 'auth', '0005_alter_user_last_login_null', '2023-04-28 10:01:41.204389'),
	(12, 'auth', '0006_require_contenttypes_0002', '2023-04-28 10:01:41.279394'),
	(13, 'auth', '0007_alter_validators_add_error_messages', '2023-04-28 10:01:41.361686'),
	(14, 'auth', '0008_alter_user_username_max_length', '2023-04-28 10:01:41.695807'),
	(15, 'auth', '0009_alter_user_last_name_max_length', '2023-04-28 10:01:42.241595'),
	(16, 'auth', '0010_alter_group_name_max_length', '2023-04-28 10:01:42.675015'),
	(17, 'auth', '0011_update_proxy_permissions', '2023-04-28 10:01:42.787067'),
	(18, 'auth', '0012_alter_user_first_name_max_length', '2023-04-28 10:01:43.042847'),
	(19, 'sessions', '0001_initial', '2023-04-28 10:01:44.302365'),
	(20, 'ServicioEducacion', '0002_cuentaalumnos_delete_tbalumno', '2023-04-28 10:24:13.228885'),
	(21, 'ServicioEducacion', '0003_rename_cuentaalumnos_cuentalumnos_and_more', '2023-04-28 10:26:35.536350'),
	(22, 'ServicioEducacion', '0004_tbalumno_tbdeudasalumno_tbpagosalumno_and_more', '2023-04-29 08:14:33.522979'),
	(23, 'ServicioEducacion', '0005_tbcuenta', '2023-06-10 07:36:16.131179');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `tbalumno` (
  `CodigoAlumno` varchar(255) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Apellido` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  PRIMARY KEY (`CodigoAlumno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `tbalumno` DISABLE KEYS */;
INSERT INTO `tbalumno` (`CodigoAlumno`, `Nombre`, `Apellido`, `Email`) VALUES
	('2020066321', 'Erick', 'Mamani', 'emm@gmail.com'),
	('2051889630', 'Mauricio', 'Lima', 'maumamani@upt.pe');
/*!40000 ALTER TABLE `tbalumno` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `tbcuenta` (
  `CodigoCuenta` varchar(255) NOT NULL,
  `Monto` decimal(10,2) NOT NULL,
  `Divisa` varchar(255) NOT NULL,
  `fkCodigoAlumno_id` varchar(255) NOT NULL,
  PRIMARY KEY (`CodigoCuenta`),
  KEY `tbCuenta_fkCodigoAlumno_id_130d820a_fk_tbAlumno_CodigoAlumno` (`fkCodigoAlumno_id`),
  CONSTRAINT `tbCuenta_fkCodigoAlumno_id_130d820a_fk_tbAlumno_CodigoAlumno` FOREIGN KEY (`fkCodigoAlumno_id`) REFERENCES `tbalumno` (`CodigoAlumno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `tbcuenta` DISABLE KEYS */;
INSERT INTO `tbcuenta` (`CodigoCuenta`, `Monto`, `Divisa`, `fkCodigoAlumno_id`) VALUES
	('724277272', 5060.69, 'EUR', '2020066321'),
	('799898156', 472.60, 'USD', '2051889630');
/*!40000 ALTER TABLE `tbcuenta` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `tbdeudasalumno` (
  `CodigoDeuda` int(11) NOT NULL AUTO_INCREMENT,
  `CantidadDeuda` decimal(10,2) NOT NULL,
  `FechaVencimiento` date NOT NULL,
  `Estado` tinyint(1) NOT NULL,
  `fkCodigoAlumno_id` varchar(255) NOT NULL,
  PRIMARY KEY (`CodigoDeuda`),
  KEY `tbDeudasAlumno_fkCodigoAlumno_id_255c0223_fk_tbAlumno_` (`fkCodigoAlumno_id`),
  CONSTRAINT `tbDeudasAlumno_fkCodigoAlumno_id_255c0223_fk_tbAlumno_` FOREIGN KEY (`fkCodigoAlumno_id`) REFERENCES `tbalumno` (`CodigoAlumno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `tbdeudasalumno` DISABLE KEYS */;
INSERT INTO `tbdeudasalumno` (`CodigoDeuda`, `CantidadDeuda`, `FechaVencimiento`, `Estado`, `fkCodigoAlumno_id`) VALUES
	(1, 750.00, '2023-04-29', 1, '2020066321'),
	(2, 950.00, '2023-04-29', 1, '2051889630'),
	(3, 5500.00, '2023-04-29', 1, '2020066321'),
	(34, 600.00, '2023-09-09', 1, '2020066321'),
	(35, 654.00, '2020-07-04', 1, '2051889630'),
	(36, 654.00, '2020-07-04', 1, '2051889630'),
	(37, 123.00, '9999-09-09', 1, '2051889630'),
	(38, 100.00, '2023-10-02', 1, '2051889630');
/*!40000 ALTER TABLE `tbdeudasalumno` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `tbpagosalumno` (
  `CodigoPago` int(11) NOT NULL AUTO_INCREMENT,
  `MontoPago` decimal(10,2) NOT NULL,
  `FechaPago` date NOT NULL,
  `FKCodigoDeuda_id` int(11) NOT NULL,
  PRIMARY KEY (`CodigoPago`),
  KEY `tbPagosAlumno_FKCodigoDeuda_id_b6559c2f_fk_tbDeudasA` (`FKCodigoDeuda_id`),
  CONSTRAINT `tbPagosAlumno_FKCodigoDeuda_id_b6559c2f_fk_tbDeudasA` FOREIGN KEY (`FKCodigoDeuda_id`) REFERENCES `tbdeudasalumno` (`CodigoDeuda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `tbpagosalumno` DISABLE KEYS */;
INSERT INTO `tbpagosalumno` (`CodigoPago`, `MontoPago`, `FechaPago`, `FKCodigoDeuda_id`) VALUES
	(1, 750.00, '2023-04-29', 1),
	(3, 750.00, '2023-04-29', 2),
	(5, 950.00, '2023-04-29', 2),
	(7, 5500.00, '2023-04-29', 3),
	(8, 5500.00, '2023-04-29', 3),
	(9, 750.00, '2023-04-29', 1),
	(10, 750.00, '2023-04-29', 1),
	(11, 123.00, '2023-06-08', 34),
	(12, 123.00, '2023-06-08', 34),
	(13, 123.00, '2023-06-09', 34),
	(14, 123.00, '2023-06-09', 34),
	(15, 123.00, '2023-06-09', 34),
	(16, 123.00, '2023-06-09', 34),
	(17, 123.00, '2023-06-09', 34),
	(18, 123.00, '2023-06-09', 34),
	(19, 123.00, '2023-06-09', 34),
	(20, 123.00, '2023-06-09', 34),
	(21, 123.00, '2023-06-09', 34),
	(22, 123.00, '2023-06-09', 34),
	(23, 123.00, '2023-06-09', 34),
	(24, 123.00, '2023-06-09', 34),
	(25, 123.00, '2023-06-09', 34),
	(26, 123.00, '2023-06-10', 34),
	(27, 654.00, '2023-06-10', 35);
/*!40000 ALTER TABLE `tbpagosalumno` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
