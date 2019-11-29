import React from 'react';
import repository from '../../../../services/repositories'

import './style.scss';

class SideBar extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      repo: ""
    };

    this.ENTER_KEY = 13;

    this.send = this.send.bind(this);
    this.onChange = this.onChange.bind(this);
  }

  onChange(event) {
    const { value } = event.target;
    this.setState({
      repo: value,
      error: false,
    });
  }

  async send(event) {
    const { repo } = this.state;
    const { getData } = this.props;

    if (event.keyCode === this.ENTER_KEY) {

      event.preventDefault();
      event.target.value = "";

      await repository.postRepository(repo)
        .catch(error => {
            const { data } = error.response

            this.setState({
              error: true
            });

            alert(data.detail || data[0])
        });

      getData();
    }

  }

  render() {
    return (
      <div className="sidebar">
        <form>
          <label>Search one of yours repositories</label>
          <input
            type='text'
            placeholder='User/Repository'
            onChange={this.onChange}
            onKeyDown={this.send}
            />
        </form>
      </div>
    );
  }
}

export default SideBar;
