/**
 * Created by storm on 2017/5/17.
 */
import axios from 'axios';

export const queryLine = () => {
    return axios.get('http://127.0.0.1:5000/line/query');
};

export const getLineHeat = (params) => {
    return axios.get('http://127.0.0.1:5000/line/heat', { params: {lid: params}});
};

export const getTgHeat = (params) => {
    return axios.get('http://127.0.0.1:5000/tg/heat', { params: {tgno: params} });
};

export const getTgEq = (params) => {
    return axios.get('http://127.0.0.1:5000/tg/eq', { params: params });
};

export const getTopTqData = (param) => {
    return axios.get('http://127.0.0.1:5000/tq/topTq', { params: {topk: param} });
};

export const getTgWithinCircle = (params) => {
    return axios.get('http://127.0.0.1:5000/tg/incircle', { params: params });
};

export const getTgWithinBox = (params) => {
    return axios.get('http://127.0.0.1:5000/tg/inbox', { params: params });
};

export const getUserByType = (param) => {
    return axios.get('http://127.0.0.1:5000/user/bytype', { params: {type: param} });
};

export const getUserInShape = (params) => {
    return axios.get('http://127.0.0.1:5000/user/inshape', { params: params });
};

export const getUserInCircle = (params) => {
    return axios.get('http://127.0.0.1:5000/user/incircle', { params: params });
};

export const getUserInBox = (params) => {
    return axios.get('http://127.0.0.1:5000/user/inbox', { params: params });
};

export const getCluster = (params) => {
    return axios.get('http://127.0.0.1:5000/cluster', { params: params });
};

export const getTest = () => {
    return axios.get('http://127.0.0.1:5000/hello', {params: {name: 'hx', age: 25}});
};
