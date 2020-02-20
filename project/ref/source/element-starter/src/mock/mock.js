/**
 * Created by storm on 2017/5/18.
 */
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import { lines, linesHeat, heatData, residentHeatData, businessHeatData } from './data/data';

export default {
    bootstrap() {
        let mock = new MockAdapter(axios);

        mock.onGet('/line/query').reply(200, lines);

        mock.onGet('/lineHeat').reply((config) => {
            let id = config.params;
            return new Promise(function (resolve, reject) {
                setTimeout(function () {
                    if (id in linesHeat) {
                        resolve([200, {data: linesHeat[id]}]);
                    } else {
                        resolve([200, {data: 'no line'}]);
                    }
                }, 1000);
            });
            // return linesHeat[id];
        });

        mock.onGet('/tq/heatData').reply(200, heatData);

        mock.onGet('/user/residentData').reply(200, residentHeatData);

        mock.onGet('/user/businessData').reply(200, businessHeatData);
    }
};