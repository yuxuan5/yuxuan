/**
 * Created by storm on 2017/5/3.
 */
import MainCharts from '../components/main-charts.vue'
import LtCharts from '../components/lt-charts.vue'
import UserCharts from '../components/user-charts.vue'
import PositionCharts from '../components/position-charts.vue'

let routes = [
    {
        path: '/mainCharts',
        component: MainCharts
    },
    {
        path: '/ltCharts',
        component: LtCharts
    },
    {
        path: '/userCharts',
        component: UserCharts
    },
    {
        path: '/positionCharts',
        component: PositionCharts
    }
];

export default routes;
