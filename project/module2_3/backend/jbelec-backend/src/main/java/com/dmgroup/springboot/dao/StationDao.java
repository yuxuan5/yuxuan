package com.dmgroup.springboot.dao;

import java.util.List;

import org.springframework.data.domain.Pageable;

import com.dmgroup.springboot.pojo.Station;

public interface StationDao {
	
	List<Station> findALL();
	
	Station getStation(String _id);
	
	void update(Station station);
	
	void insert(Station station);
	
	void insertAll(List<Station> stations);
	
	void remove(String _id);
	
	List<Station> findByPage(Station station, Pageable pageable);
}
