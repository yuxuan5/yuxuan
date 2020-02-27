package com.dmgroup.springboot.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import com.dmgroup.springboot.dao.ProtectDao;
import com.dmgroup.springboot.pojo.Protect;
import com.dmgroup.springboot.service.ProtectService;

@Service("protectService")
public class ProtectServiceImpl implements ProtectService{

	@Autowired
	private ProtectDao protectDao;
	
	@Override
	public List<Protect> findAll() {
		return protectDao.findAll();
	}

	@Override
	public Protect getProtect(int FIBER_ID) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void update(Protect protect) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void insert(Protect protect) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void insertAll(List<Protect> protect) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void remove(int PROTECT_ID) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public List<Protect> findByPage(Protect protect, Pageable pageable) {
		// TODO Auto-generated method stub
		return null;
	}

}
