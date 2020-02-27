package com.dmgroup.springboot.dao.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;
import org.springframework.stereotype.Repository;

import com.dmgroup.springboot.dao.FiberDao;
import com.dmgroup.springboot.pojo.Fiber;

@Repository("fiberDao")
public class FiberDaoImpl implements FiberDao{

	@Autowired
	private MongoTemplate mongoTemplate;
	
	@Override
	public List<Fiber> findAll() {
		return mongoTemplate.findAll(Fiber.class,"fiber_light_path");
	}

	@Override
	public Fiber getFiber(int FIBER_ID) {
		// TODO Auto-generated method stub
		System.out.println("dao");
		Fiber fiber=mongoTemplate.findOne(new Query(Criteria.where("FIBER_ID").is(FIBER_ID)), Fiber.class,"fiber_light_path");
		if(fiber==null){
			System.out.println("null");
			return null;
		}
		return fiber;	
	}

	@Override
	public void update(Fiber fiber) {

		Criteria criteria = Criteria.where("_id").is(fiber.get_id());
		Query query = new Query(criteria);
		//Update update = Update.update("FIBER_NAME", fiber.getFIBER_NAME()).set("FIBER_FULL_NAME",  fiber.getFIBER_FULL_NAME());
		//mongoTemplate.updateMulti(query, update, Station.class);
		// TODO 
		
	}

	@Override
	public void insert(Fiber fiber) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void insertAll(List<Fiber> fiber) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void remove(int FIBER_ID) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public List<Fiber> findByPage(Fiber fiber, Pageable pageable) {
		// TODO Auto-generated method stub
		return null;
	}

}
