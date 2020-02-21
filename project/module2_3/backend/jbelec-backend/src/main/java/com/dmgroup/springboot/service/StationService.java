package com.dmgroup.springboot.service;

import java.util.List;

import org.springframework.data.domain.Pageable;

import com.dmgroup.springboot.pojo.Station;

public interface StationService {
	List<Station> findAll();
	
	Station getStation(String _id);
	
	void update(Station station);
	
	void insert(Station station);
	
	void insertAll(List<Station> station);
	
	void remove(String _id);
	
	List<Station> findByPage(Station station, Pageable pageable);

}
