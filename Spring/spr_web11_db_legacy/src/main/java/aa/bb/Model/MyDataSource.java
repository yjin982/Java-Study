package aa.bb.Model;

import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Repository;

@Repository("dataSource")
public class MyDataSource extends DriverManagerDataSource{
	public MyDataSource() {
		setDriverClassName("org.mariadb.jdbc.Driver");
		setUrl("jdbc:mysql://localhost:3306/test");
		setUsername("root");
		setPassword("123");
	}
}
