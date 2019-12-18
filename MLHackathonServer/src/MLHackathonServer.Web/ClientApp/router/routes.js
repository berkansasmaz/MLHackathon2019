import HomePage from 'components/pages/home-page'
import Forbidden from 'components/root/forbidden';

export const routes = [
  {
	   name: 'home',
	   path: '/', 
	   component: HomePage, 
	   display: 'Home', 
	   icon: 'home' 
	},
	{
		divider: true,
		path: ''
	},
	{
		name: 'account-view',
		path: '/Identity/Account/Manage',
		display: 'Account',
		icon: 'user-circle'
	  },
	{
		name: 'forbidden',
		path: '/forbidden',
		hidden: true,
		component: Forbidden
	}
 
]
