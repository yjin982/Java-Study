package pack.member;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class MemberMgr {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	private DataSource ds;
	
	public MemberMgr() { ////생성자 DB연결
		try { 
			Context context = new InitialContext();
			ds = (DataSource)context.lookup("java:comp/env/jdbc_maria");
		} catch (Exception e) {
			System.out.println("board manager err");
			e.printStackTrace();
		}
	}
	
	public ArrayList<ZipCodeDto> zipcodeRead(String dongName){ //우편번호 검색,읽기
		ArrayList<ZipCodeDto> list = new ArrayList<ZipCodeDto>();
		String sql = "select * from ziptab where area3 like ?";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, dongName + "%");
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				ZipCodeDto dto = new ZipCodeDto();
				dto.setZipcode(rs.getString("zipcode"));
				dto.setArea1(rs.getString("area1"));
				dto.setArea2(rs.getString("area2"));
				dto.setArea3(rs.getString("area3"));
				dto.setArea4(rs.getString("area4"));
				list.add(dto);
			}
		} catch (Exception e) {
			System.out.println("zipcodeRead err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("zipcodeRead close err");
				e.printStackTrace();
			}
		}
		return list;
	}
	
	public boolean checkId(String id) { //아이디 중복체크
		boolean b = false;
		String sql = "select id from member where id=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, id);
			rs = pstmt.executeQuery();
			b = rs.next();
			
			
		} catch (Exception e) {
			System.out.println("checkId err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("checkId close err");
				e.printStackTrace();
			}
		}
		return b;
	}
	
	public boolean memberInsert(MemberBean bean) { //회원가입
		boolean b = false;
		String sql = "insert into member values(?,?,?,?,?,?,?,?)";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, bean.getId());
			pstmt.setString(2, bean.getPasswd());
			pstmt.setString(3, bean.getName());
			pstmt.setString(4, bean.getEmail());
			pstmt.setString(5, bean.getPhone());
			pstmt.setString(6, bean.getZipcode());
			pstmt.setString(7, bean.getAddress());
			pstmt.setString(8, bean.getJob());
			
			if(pstmt.executeUpdate() > 0) {
				b = true;
			}
			
		}catch (Exception e) {
			System.out.println("checkId err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("checkId close err");
				e.printStackTrace();
			}
		}
		return b;
	}
	
	public boolean loginCheck (String id, String passwd) { //로그인
		boolean b = false;
		String sql = "select id, passwd from member where id=? and passwd=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, id);
			pstmt.setString(2, passwd);
			rs = pstmt.executeQuery();
			b = rs.next();
			
		}catch (Exception e) {
			System.out.println("loginCheck err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("loginCheck close err");
				e.printStackTrace();
			}
		}
		return b;
	}
	
	public MemberBean getMember(String id) { //쇼핑몰에서 개인 로그인 후 각 id로 수정하기
		MemberBean bean = null;
		String sql = "select * from member where id=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, id);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				bean = new MemberBean();
				bean.setId(rs.getString("id"));
				bean.setPasswd(rs.getString("passwd"));
				bean.setName(rs.getString("name"));
				bean.setEmail(rs.getString("email"));
				bean.setPhone(rs.getString("phone"));
				bean.setZipcode(rs.getString("zipcode"));
				bean.setAddress(rs.getString("address"));
				bean.setJob(rs.getString("job"));
			}
		}catch (Exception e) {
			System.out.println("getMember err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("getMember close err");
				e.printStackTrace();
			}
		}
		return bean;
	}
	
	public boolean memberUpdate(MemberBean bean, String id) { //회원 정보 수정
		boolean b = false;
		String sql = "update member set passwd=?, name=?, phone=?, email=?, address=?, zipcode=?, job=? where id=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, bean.getPasswd());
			pstmt.setString(2, bean.getName());
			pstmt.setString(3, bean.getPhone());
			pstmt.setString(4, bean.getEmail());
			pstmt.setString(5, bean.getAddress());
			pstmt.setString(6, bean.getZipcode());
			pstmt.setString(7, bean.getJob());
			pstmt.setString(8, id);
			
			if(pstmt.executeUpdate() > 0) b = true;
			
		}catch (Exception e) {
			System.out.println("memberUpdate err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("memberUpdate close err");
				e.printStackTrace();
			}
		}
		return b;
	}
	
	// 관리자 로그인 관련
	public boolean adminLoginCheck(String id, String passwd) {
		boolean b = false;
		
		try {
			String sql = "select * from admin where admin_id = ? and admin_passwd = ?";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, id);
			pstmt.setString(2, passwd);
			rs = pstmt.executeQuery();
			
			b = rs.next();
			
		} catch (Exception e) {
			System.out.println("adminLoginCheck err : " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
		
		return b;
	}
	
}
