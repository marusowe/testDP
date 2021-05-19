CREATE DATABASE test_dp;
CREATE USER 'test_dp_user'@'%' IDENTIFIED WITH mysql_native_password BY '123';
GRANT ALL ON *.* TO 'test_dp_user'@'%';
