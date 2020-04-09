package pack.model;

import java.util.List;
import org.springframework.dao.DataAccessException;
import pack.controller.SangpumBean;

public interface SangpumInter {
	List<SangpumDto> selectList() throws DataAccessException;
	List<SangpumDto> search(SangpumBean bean) throws DataAccessException;
}
