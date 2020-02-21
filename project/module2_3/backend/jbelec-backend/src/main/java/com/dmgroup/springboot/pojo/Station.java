package com.dmgroup.springboot.pojo;

import java.io.Serializable;

import org.springframework.data.annotation.Id;

public class Station implements Serializable{
	private static final long serialVersionUID = 1L;
	
	@Id
	private String _id;
	private String STATION_NAME;
	private String POWER_LEVEL;
	private double x;
	private double y;
	
	public Station(String _id, String STATION_NAME, String POWER_LEVEL, double x, double y) {
		this._id = _id;
		this.STATION_NAME = STATION_NAME;
		this.POWER_LEVEL = POWER_LEVEL;
		this.x = x;
		this.y = y;
	}
	
	public String get_id() {
		return _id;
	}
	
	public void set_id(String _id) {
		this._id = _id;
	}
	
	public String getSTATION_NAME() {
		return STATION_NAME;
	}
	
	public void setSTATION_NAME(String STATION_NAME) {
		this.STATION_NAME = STATION_NAME;
	}
	
	public String getPOWER_LEVEL() {
		return POWER_LEVEL;
	}
	
	public void setPOWER_LEVEL(String POWER_LEVEL) {
		this.POWER_LEVEL = POWER_LEVEL;
	}
	
	public double getx() {
		return x;
	}
	
	public void setx(double x) {
		this.x = x;
	}
	
	public double gety() {
		return y;
	}
	
	public void sety(double y) {
		this.y = y;
	}
	
	public Station() {
		super();
	}
	
	public String toString() {
		return "Station [_id=" + _id + ", STATION_NAME=" + STATION_NAME + ", POWER_LEVEL=" + POWER_LEVEL + ", x=" + x + ", y=" + y;
	}
}