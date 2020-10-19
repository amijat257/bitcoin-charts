import Fetch from 'isomorphic-unfetch';
import Layout from '../components/Layout';
import Prices from '../components/Prices';


const Index = (props) => (
    <Layout>
        <div>
            <h1>Top 20 Markets by Volume</h1>
            <p>In the list below you can se the latest results for volume by market.</p>
            <Prices records={props.records}/>
        </div>
    </Layout>
);


Index.getInitialProps = async function() {
    const data = await fetch(process.env.API_URL + '/api/records/top/')
        .then((response) => response.json())
    return {
        records: data
    };
}
export default Index;