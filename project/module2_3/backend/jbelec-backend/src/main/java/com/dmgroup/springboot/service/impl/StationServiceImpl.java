package com.dmgroup.springboot.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import com.dmgroup.springboot.pojo.Station;
import com.dmgroup.springboot.dao.StationDao;
import com.dmgroup.springboot.service.StationService;

@Service("stationService")
public class StationServiceImpl implements StationService {
	
	@Autowired
	private StationDao stationDao;
	
	@Override
	public List<Station> findAll() {

		return stationDao.findALL();
	}

	@Override
	public Station getStation(int STATION_ID) {

		return stationDao.getStation(STATION_ID);
	}

	@Override
	public void update(Station station) {
		stationDao.update(station);
		
	}

	@Override
	public void insert(Station station) {
		stationDao.insert(station);
		
	}

	@Override
	public void insertAll(List<Station> station) {
		stationDao.insertAll(station);
		
	}

	@Override
	public void remove(int STATION_ID) {
		stationDao.remove(STATION_ID);
		
	}

	@Override
	public List<Station> findByPage(Station station, Pageable pageable) {
		
		return stationDao.findByPage(station, pageable);
	}

}
