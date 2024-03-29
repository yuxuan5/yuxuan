package com.dmgroup.springboot.service;

import java.util.List;

import org.springframework.data.domain.Pageable;

import com.dmgroup.springboot.pojo.Protect;

public interface ProtectService {
	List<Protect> findAll();
	
	Protect getProtect(int FIBER_ID);
	
	void update(Protect protect);
	
	void insert(Protect protect);
	
	void insertAll(List<Protect> protect);
	
	void remove(int PROTECT_ID);
	
	List<Protect> findByPage(Protect protect, Pageable pageable);

}
