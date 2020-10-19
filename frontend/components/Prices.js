import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import CurrencyFlag from 'react-currency-flags';

class Prices extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            items: props.records
        }
    }

    render() {
        var {items} = this.state;
        return (
            <div>
                <TableContainer>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell><strong>Market Symbol</strong></TableCell>
                                <TableCell align="right"><strong>Currency Code</strong></TableCell>
                                <TableCell align="right"><strong>Currency Name</strong></TableCell>
                                <TableCell align="right"><strong>Volume Name</strong></TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {items.map((record) => (
                                <TableRow key={record.market.symbol}>
                                    <TableCell component="th" scope="row">
                                        {record.market.symbol}
                                    </TableCell>
                                    <TableCell align="right">{
                                        record.market.currency.code
                                    }
                                        {
                                            <CurrencyFlag currency={record.market.currency.code} size="md"
                                                          style={{marginLeft: 20, border: "1px solid"}}/>
                                        }</TableCell>
                                    <TableCell align="right">{record.market.currency.name}</TableCell>
                                    <TableCell align="right">{record.volume}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        );
    }
}

export default Prices;
