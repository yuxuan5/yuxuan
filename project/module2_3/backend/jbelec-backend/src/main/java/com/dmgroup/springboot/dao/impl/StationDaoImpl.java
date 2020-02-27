package com.dmgroup.springboot.dao.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;
import org.springframework.stereotype.Repository;

import com.dmgroup.springboot.dao.StationDao;
import com.dmgroup.springboot.pojo.Station;;

@Repository("stationDao")
public class StationDaoImpl implements StationDao {
	
	@Autowired
	private MongoTemplate mongoTemplate;
	
	@Override
	public List<Station> findALL() {
	 
		return mongoTemplate.findAll(Station.class);
	}

	@Override
	public Station getStation(int STATION_ID) {
		
		return mongoTemplate.findOne(new Query(Criteria.where("STATION_ID").is(STATION_ID)), Station.class);
	}

	@Override
	public void update(Station station) {
		Criteria criteria = Criteria.where("_id").is(station.get_id());
		Query query = new Query(criteria);
		Update update = Update.update("STATION_NAME", station.getSTATION_NAME()).set("POWER_LEVEL",  station.getPOWER_LEVEL()).set("x", station.getx()).set("y", station.gety());
		mongoTemplate.updateMulti(query, update, Station.class);
		
	}

	@Override
	public void insert(Station station) {

		mongoTemplate.insert(station);
		
	}

	@Override
	public void insertAll(List<Station> stations) {
		
		mongoTemplate.insertAll(stations);
		
	}

	@Override
	public void remove(int STATION_ID) {
		Criteria criteria = Criteria.where("STATION_ID").is(STATION_ID);
		Query query = new Query(criteria);
		mongoTemplate.remove(query, Station.class);
	}

	@Override
	public List<Station> findByPage(Station station, Pageable pageable) {
		Query query = new Query();
		if(station != null && station.getSTATION_NAME() != null) {
			// 模糊查询
			query = new Query(Criteria.where("STATION_NAME").regex("^" + station.getSTATION_NAME()));
		}
		List<Station> list = mongoTemplate.find(query.with(pageable), Station.class);
		return list;
	}

}
