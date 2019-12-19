import HomePage from 'components/pages/home-page'
import Comment from 'components/pages/comment'
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
		name: 'comment',
		path: '/comment', 
		component: Comment, 
		display: 'Comment', 
		icon: 'pen' 
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
