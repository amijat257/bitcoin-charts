import Link from 'next/link';

const Navbar = () => (
   <nav className="navbar navbar-expand navbar-dark bg-dark mb-4">
       <div className="container">
           <a className="navbar-brand" href="#">
               <img style={{width: "4%", paddingBottom: "12px"}} src="https://utz.org/wp-content/uploads/2017/04/Globe_Africa_white-700x700.png"/>
               <span style={{fontSize: "2rem", paddingLeft: "15px"}}><strong>Currency Market</strong></span>
           </a>
        <div className="collapse navbar-collapse">
        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <Link href="/"><a className="nav-link"><strong>Markets</strong></a></Link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
);

export default Navbar;