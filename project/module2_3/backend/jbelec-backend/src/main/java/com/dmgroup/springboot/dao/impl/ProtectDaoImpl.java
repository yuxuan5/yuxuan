package com.dmgroup.springboot.dao.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Repository;

import com.dmgroup.springboot.dao.ProtectDao;
import com.dmgroup.springboot.pojo.Protect;

@Repository("ProtectDao")
public class ProtectDaoImpl implements ProtectDao{
	
	@Autowired
	private MongoTemplate mongoTemplate;
	
	@Override
	public List<Protect> findAll() {
		//System.out.println("here we go");
		return mongoTemplate.findAll(Protect.class,"protect");
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
